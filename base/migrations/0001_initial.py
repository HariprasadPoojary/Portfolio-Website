# Generated by Django 3.0.8 on 2021-01-10 17:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('phone', models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator(message='Please eneter phone in correct format', regex='([+]?\\d{1,2}[.\\s]?)?(\\d{3}[.-]?){2}\\d{4}')])),
                ('message', models.TextField()),
            ],
        ),
    ]
