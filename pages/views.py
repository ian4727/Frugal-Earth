from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse ("<h1>hello</h1>")
    return render(request, "index.html", {})

def signin(request):
        return render(request, "signin.html", {})    

def signup(request):
    return render(request, "signup.html", {})    