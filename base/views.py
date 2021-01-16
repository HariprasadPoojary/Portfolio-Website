from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.conf import settings
import os
from django.core.mail import BadHeaderError, send_mail


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


def download_cv(request):
    # Access the media_root directory from settings and join the path with pdf
    # to open the file, read as binary(bcoz it's pdf) and return in HttpResponse

    with open(os.path.join(settings.MEDIA_ROOT, "cv/Hari_CV_v1.5.pdf"), "rb") as pd:
        response = HttpResponse(pd.read(), content_type="application/pdf")
        response[
            "Content-Disposition"
        ] = "attachment; filename=Hariprasad_Poojary_CV.pdf"
        return response
