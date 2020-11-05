from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):
    if request.method == 'POST':
        acc = Account()
        user = User()
        acc.User = request.POST['user']
        user.username = acc.User
        acc.Password = request.POST['pass']
        user.set_password(request.POST['pass'])
        acc.Email = request.POST['email']
        user.email = acc.Email
        acc.save()
        user.save()
        return redirect('signin')
    else:
        return render(request,'signup.html')  

def signin(request):
    if request.method == 'POST':
        user = User()
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('search')
        else:
            msg = "Invalid username or password."    
            return render(request,'signin.html',context = {'msg':msg,'user':user})
    else:
        return render(request,'signin.html')

