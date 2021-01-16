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


def send_email(request):
    name = request.POST.get("name")
    from_email = request.POST.get("email")
    subject = request.POST.get("subject")
    subject = "[Django-Portfolio] " + subject
    phone = request.POST.get("phone")
    message = request.POST.get("message")
    message_full = f""" 
        Hello Hari,

            {name}, email: {from_email} wants to connect with you.
            Phone: {phone}
            Message: {message}
    """
    if name and from_email:
        try:
            send_mail(subject, message_full, from_email, ["hari.j.wayne@gmail.com"])
            return "I have received your details, see you soon 🙋🏽‍♂️"
        except BadHeaderError:
            return "Something went wrong😅, please contact me on below ⬇"
    return "Please fill something💢"


def contact(request):
    contact_form = ContactMeForm()
    email_res = ""
    if request.method == "POST":
        contact_form = ContactMeForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            email_res = send_email(request)
            # return redirect("index")
    context = {
        "contact_form": contact_form,
        "email_res": email_res,
    }
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
