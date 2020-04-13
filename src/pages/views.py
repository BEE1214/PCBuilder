from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    print("request=",request)
    print("args=",args)
    print("kwargs=",kwargs)
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    print("request=",request)
    print("args=",args)
    print("kwargs=",kwargs)
    information = {
        "Name":"Adam Dvorsky",
        "Email":"something@gmail.com",
        "Phone_Number": "+420736432940"
    }
    return render(request, "about.html", information)

def build_view(request, *args, **kwargs):
    print("request=",request)
    print("args=",args)
    print("kwargs=",kwargs)
    return render(request, 'build.html', {})

def profile_view(request, *args, **kwargs):
    print("request=",request)
    print("args=",args)
    print("kwargs=",kwargs)
    return render(request, 'profile.html', {})