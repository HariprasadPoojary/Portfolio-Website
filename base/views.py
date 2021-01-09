from django.http import request
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, "base/index.html")


def about(request):
    return render(request, "base/about.html")


def work(request):
    return render(request, "base/work.html")


def contact(request):
    return render(request, "base/contact.html")
