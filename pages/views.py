from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Posts
from .forms import CreateUserForm

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
           user = User.objects.get(username=username)
        except:
           messages.error(request, 'Username invalid')   

        user= authenticate(request, username=username, password=password)

        if user is not None:
           login(request, user)
           return redirect('home')
        else:
            messages.error(request, 'Invalid username or Password')
    return render(request, 'pages/signin.html')    

def signout(request):
    logout(request)
    return redirect('home')    



def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
            
    return render(request, "pages/signup.html", {"form":form})    

 