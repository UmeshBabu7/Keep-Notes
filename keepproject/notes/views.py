from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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


def home_page(request):
    return render(request,'home.html')


def settings(request):
    return render(request,'settings.html')


def loggedout(request):
    return render(request,'loggedout.html')


def update(request):
    return render(request,'update.html')
