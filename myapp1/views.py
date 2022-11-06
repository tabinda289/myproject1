import email
from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import Feature

# Create your Views here
def index(request):
    features=Feature.objects.all()
    return render(request,'index.html',{'features':features })

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"email Already exists")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "name is already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password2)
                user.save()
                return redirect('Login')
        else:
            messages.info(request, "passworrd already exists")
            return redirect('register')
    else:
        return render(request,'register.html')    
         

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
         
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            message.info(request,'Credential invalid')
            return redirect('login')
    else:
         return render(request,'login.html')

def counter(request):
    posts = [1,2,3,4,5,6,'kanwal','aruba','hifza','Tabinda']
    #text=request.POST['text']
    #amount_of_words=len(text.split())
    return render(request,'counter.html',{'posts':posts})
    
def logout(request):
    auth.logout(request)
    return redirect('/')
    

def post(request,pk):
    return render(request,'post.html',{'pk':pk})