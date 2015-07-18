from django.shortcuts import render
import operator
from django.db.models import Avg, Count
from .models import Engineer,Rating
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView


class EngineerCreate(CreateView):
    model = Engineer
    fields = ['name', 'version']
    # success_url = '/ratings/'

# class ProjectCreate(CreateView):
#     model = Project

class RatingCreate(CreateView):
    model = Rating
    fields = ['QL1_1_inc', 'QL1_1_loa', 'QL1_1_exp',
              'QL1_2_inc', 'QL1_2_loa', 'QL1_2_exp',
              'QL1_3_inc', 'QL1_3_loa', 'QL1_3_exp',
              'QL2_1_inc', 'QL2_1_loa', 'QL2_1_exp',
              'QL2_2_inc', 'QL2_2_loa', 'QL2_2_exp',
              'QL2_3_inc', 'QL2_3_loa', 'QL2_3_exp',
              'QL2_4_inc', 'QL2_4_loa', 'QL2_4_exp',
              'QL2_5_inc', 'QL2_5_loa', 'QL2_5_exp',
              'QL2_6_inc', 'QL2_6_loa', 'QL2_6_exp',
              'QL3_1_inc', 'QL3_1_loa', 'QL3_1_exp',
              'QL3_2_inc', 'QL3_2_loa', 'QL3_2_exp',
              'QL3_3_inc', 'QL3_3_loa', 'QL3_3_exp',]

