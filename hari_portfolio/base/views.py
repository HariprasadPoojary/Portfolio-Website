from django.http import request
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, "base/index.html")


def more(request):
    return render(request, "base/main.html")
