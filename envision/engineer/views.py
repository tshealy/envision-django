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
from .forms import RatingForm

class EngineerCreate(CreateView):
    model = Engineer
    fields = ['name', 'version']
    success_url = '/ratings/'

    def get_success_url(self):
        return reverse("engineer_detail", kwargs={
            'pk':self.object.pk,
        })

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


