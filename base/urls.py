# from os import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("work/", views.work, name="work"),
    path("contact/", views.contact, name="contact"),
    path("download/", views.download_cv, name="download_cv"),
]
