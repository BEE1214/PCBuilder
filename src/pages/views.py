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
    return render(request, "about.html", {})

def component_view(request, *args, **kwargs):
    print("request=",request)
    print("args=",args)
    print("kwargs=",kwargs)
    return render(request, 'component.html', {})

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