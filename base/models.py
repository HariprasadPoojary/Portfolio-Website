from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class ContactMeInfo(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=150)
    # Regex class to validate phone number
    phone_regex = RegexValidator(
        regex=r"([+]?\d{1,2}[.\s]?)?(\d{3}[.-]?){2}\d{4}",
        message="Please eneter phone in correct format",
    )
    phone = models.CharField(
        validators=[phone_regex], max_length=13, blank=True, null=True
    )
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}, {self.email}"

