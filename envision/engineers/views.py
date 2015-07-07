from django.shortcuts import render
import operator
from django.db.models import Avg, Count
from .models import Engineer, Project, Rating
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView



# class LoginRequiredMixin(object):
#     @classmethod
#     def as_view(cls, **initkwargs):
#         view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
#         return login_required(view)
#
#
# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect('/index/')
#
#


class EngineerCreate(CreateView):
    model = Engineer
    fields = ['name', 'version']
    # success_url = '/index/'