from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Note
from .forms import NoteCreationForm,NoteUpdateForm,AccountSettingsForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
    return render(request,'index.html')


def register(request):
    form=UserCreationForm()

    if request.method =='POST':
        form=UserCreationForm(request.POST)

        
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully..")
            return redirect('notes:login')
        
    context={
            'form':form
        }

    return render(request,'register.html',context)

@login_required
def home_page(request):
    notes=Note.objects.all()
    form=NoteCreationForm()

    if request.method =='POST':
        form=NoteCreationForm(request.POST)

        if form.is_valid():
            note_obj=form.save(commit=False)
            note_obj.author=request.user
            note_obj.save()

            return redirect('notes:home_page')
    
    context={
        'notes':notes,
        'form':form
    }

    return render(request,'home.html',context)

@login_required
def settings(request):
    user=request.user

    form=AccountSettingsForm(instance=user)

    if request.method =="POST":
        user.username=request.POST.get("username")
        user.first_name=request.POST.get("first_name")
        user.last_name=request.POST.get("last_name")

        user.save()

        messages.success(request,"Account Updated Successfully")
        return redirect("notes:settings")

    context={
            'form':form,
            'user':user
        }
    return render(request,'settings.html',context)


def loggedout(request):
    return render(request,'loggedout.html')

@login_required
def update(request,id):
    note_to_update=Note.objects.get(id=id)
    form=NoteUpdateForm(instance=note_to_update)

    if request.method =="POST":
        form=NoteUpdateForm(request.POST)

        if form.is_valid():
            note_to_update.title=form.cleaned_data["title"]
            note_to_update.description=form.cleaned_data["description"]

            note_to_update.save()

            return redirect('notes:home_page')
    context={
        'note':note_to_update,
        'form':form
    }
    return render(request,'update.html',context)

@login_required
def delete(request,id):
    note_to_delete=Note.objects.get(id=id)

    note_to_delete.delete()

    return redirect('notes:home_page')


