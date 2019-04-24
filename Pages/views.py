from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def fortigate_view(request, *args, **kwargs):
    return render(request, "FortiGate.html", {})


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "home.html", {})


def base_view(request, *args, **kwargs):
    return render(request, "base.html", {})


def configure_view(request, *args, **kwargs):
    return render(request, "configure.html", {})


def copy_view(request, *args, **kwargs):
    return render(request, "copy.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

