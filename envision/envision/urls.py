"""envision URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from engineer import views as engineer_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),
    url(r'^index/$', TemplateView.as_view(template_name="index.html")),
    url(r'^name/$',engineer_views.EngineerCreate.as_view(), name='engineer_add'),
    url(r'^ratings/$',engineer_views.RatingCreate.as_view(), name='rating_add'),
    #url(r'^index/', CreateView.as_view()),
    # url('^', CreateView.as_view(template_name='engineer'))
    # url('^register/', CreateView.as_view(
    #         template_name='engineer/register.html',
    #         form_class=UserCreationForm,
    #         success_url='/index/'), name= "user_register"),
    # url(r'^$', TemplateView.as_view(template_name="engineer/index.html"), name='view_index'),
]

