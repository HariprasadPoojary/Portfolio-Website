from django import forms
from django.core.validators import RegexValidator
from django.forms import widgets
from .models import ContactMeInfo


# class ContactMeForm(forms.ModelForm):
#     class Meta:
#         model = ContactMeInfo
#         fields = "__all__"


class ContactMeForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Name..."}),
        error_messages={
            "required": "Please enter your name 😐",
            "max_length": "Please enter a shorter name 😐",
        },
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email..."}),
        error_messages={"required": "Please enter an email id 😐",},
    )
    subject = forms.CharField(
        max_length=70,
        widget=forms.TextInput(attrs={"placeholder": "Subject..."}),
        error_messages={
            "required": "Please enter a Subject 😐",
            "max_length": "Please enter a shorter Subject 😐",
        },
    )
    # Regex class to validate phone number
    phone_regex = RegexValidator(
        regex=r"([+]?\d{1,2}[.\s]?)?(\d{3}[.-]?){2}\d{4}",
        message="Please enter phone in correct format",
    )
    phone = forms.CharField(
        max_length=13,
        validators=[phone_regex],
        widget=forms.TextInput(attrs={"placeholder": "Phone..."}),
        error_messages={
            "max_length": "Please enter a valid Phone Number or keep it blank 😐",
        },
        required=False,
    )
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={"placeholder": "Message...", "cols": 40, "rows": 10,}
        ),
        error_messages={"max_length": "Please enter a Shorter Message 😐"},
        required=False,
    )

