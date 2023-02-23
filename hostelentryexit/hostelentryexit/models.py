from django.db import models

class Hostel (models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

from django.db import forms

class HostelForm (forms.ModelForm):
    password = forms.CharField (widget = forms. PasswordInput)

    class Meta:
        model = Hostel


