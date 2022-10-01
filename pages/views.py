from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Posts

# Create your views here.
def home(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "index.html", {})

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
           user = User.objects.get(username=username)
        except:
           messages.error(request, 'User does not exist')   

        user= authenticate(request, username=username, password=password)

        if user is not None:
           login(request, user)
           return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')

    context = {} 
    return render(request, "signin.html", context)    

def signout(request):
    logout(request)
    return redirect('home')    

def signup(request):
    context = {}
    return render(request, "signup.html", context)    