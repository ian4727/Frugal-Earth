from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Posts

# Create your views here.
def home(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse ("<h1>hello</h1>")
    return render(request, "index.html", {})

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            email = email.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')   

        email= authenticate(request, email=email, password=password)

        if email is not None:
            login(request, email)
            return redirect('home')

    context = {} 
    return render(request, "signin.html", context)    

def signup(request):
    context = {}
    return render(request, "signup.html", context)    