__author__ = 'trippshealy'
from django import forms
from django.contrib.auth.models import User
from .models import Engineer, Rating


class EngineerForm(forms.ModelForm):
    class Meta:
        model = Engineer


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating