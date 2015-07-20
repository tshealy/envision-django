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
from django.core.urlresolvers import reverse
from .forms import RatingForm, EngineerForm

class EngineerCreate(CreateView):
    model = Engineer
    fields = ['name']
    # success_url = '/ratings/'

    def get_success_url(self):
        return reverse("pick_version", kwargs={
            'pk':self.object.pk,
        })

def pick_version(request, pk):
    engineer = Engineer.objects.get(pk=pk)
    if engineer.pk % 2 == 0:
        engineer.version = 0
    else:
        engineer.version = 1
    engineer.save()
    return redirect("engineer_detail", pk)


def display_engineer(request, pk):

    engineer = Engineer.objects.get(pk=pk)
    # engineer.rating = Rating()
    # engineer.rating.save()

    # QL1_1_loa = engineer.rating.QL1_1_loa

    if request.method == "GET":
        rating_form = RatingForm()
    elif request.method == "POST":
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.engineer = engineer
            rating.save()
            return redirect('index')

    return render(request, "engineer/rating_form.html", {'rating_form': rating_form, "engineer": engineer,})




class RatingCreate(CreateView):

    model = Rating
    fields = ['QL1_1_inc', 'QL1_1_loa', 'QL1_1_exp',
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



