from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def home_page(request):
    return render(request,'home.html')
def settings(request):
    return render(request,'settings.html')
def loggedout(request):
    return render(request,'loggedout.html')
def update(request):
    return render(request,'update.html')
