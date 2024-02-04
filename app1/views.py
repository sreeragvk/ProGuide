from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

def signup(request):
    if request.method=="POST":
        u=request.POST['u']
        p1=request.POST['p1']
        p2=request.POST['p2']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        if(p1==p2):
            # u=User.objects.create_user(username=u,password=p1,first_name=f,last_name=l,email=e)
            # u.save()
            return redirect("courses:categories")
    return render(request,'signup.html')

def user_login(request):
    if request.method=='POST':
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect("courses:categories")
        else:
            messages.error(request,"invalid credentials")
    return render(request,'login.html')
    
    
