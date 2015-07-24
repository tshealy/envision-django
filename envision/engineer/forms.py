__author__ = 'trippshealy'
from django import forms
from django.contrib.auth.models import User
from .models import Engineer, Rating


class EngineerForm(forms.ModelForm):
    name = forms.CharField()
    version = forms.CharField()

    class Meta:
        model = Engineer
        fields = ('name', 'version',)


# class ProjectForm(forms.ModelForm):
#
#     class Meta:
#         model = Project


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ['engineer', 'total_time',
            'QL1_1_inc', 'QL1_1_loa', 'QL1_1_exp',
            'QL1_2_inc', 'QL1_2_loa', 'QL1_2_exp',
            'QL2_3_inc', 'QL2_3_loa', 'QL2_3_exp',
            'QL2_5_inc', 'QL2_5_loa', 'QL2_5_exp',
            'QL2_6_inc', 'QL2_6_loa', 'QL2_6_exp',
            'QL3_3_inc', 'QL3_3_loa', 'QL3_3_exp',
            'LD1_2_inc', 'LD1_2_loa', 'LD1_2_exp',
            'LD1_4_inc', 'LD1_4_loa', 'LD1_4_exp',
            'LD2_2_inc', 'LD2_2_loa', 'LD2_2_exp',
            'NW1_2_inc', 'NW1_2_loa', 'NW1_2_exp',
            'NW2_2_inc', 'NW2_2_loa', 'NW2_2_exp',
            'NW2_3_inc', 'NW2_3_loa', 'NW2_3_exp',]


