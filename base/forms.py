from django.forms import ModelForm
from .models import ContactMeInfo


class ContactMeForm(ModelForm):
    class Meta:
        model = ContactMeInfo
        fields = "__all__"

