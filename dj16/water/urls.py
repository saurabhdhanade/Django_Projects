
from django.contrib import admin
from django.urls import path
from water import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index),
    path('', RedirectView.as_view(url = '/water')),
         ]
