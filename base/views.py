from django.http import request
from django.shortcuts import redirect, render
from django.http import HttpResponse


# Create your views here.
from .forms import ContactMeForm


def index(request):
    return render(request, "base/index.html")


def about(request):
    return render(request, "base/about.html")


def work(request):
    return render(request, "base/work.html")


def contact(request):
    contact_form = ContactMeForm()
    if request.method == "POST":
        contact_form = ContactMeForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect("index")
    context = {"contact_form": contact_form}
    return render(request, "base/contact.html", context=context)
