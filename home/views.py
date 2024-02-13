from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request,'index.html')

def user_login(request):
   
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')


        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/')
        user = authenticate(request,username=username, password=password)
        

        if user is None:
            messages.error(request, 'Invalid Password or Username')

        else:
            login(request,user)
            return redirect("/")

    return render(request,'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password == password_confirm:

            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Account created successfully.')
            return render(request,'login.html')
        else:
            messages.error(request, 'Passwords do not match. Please try again.')

    return render(request, 'register.html')

def user_logout(request):
    logout(request)
    return redirect('/')
    
# @login_required(login_url="/login/")
def packages(request):

    return render(request, 'packages.html')
    

def services(request):
    return render(request,'services.html')  

def book(request):
    return render(request,'book.html')  
def pack(request):
    return render(request,'pack.html') 
 
def starting(request):
    return render(request,'starting.html')  

def flight(request):
    return render(request,'flight.html')  

def about(request):
    return render(request,'about.html')  