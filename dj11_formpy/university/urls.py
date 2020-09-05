
from django.contrib import admin
from django.urls import path
from university import views

urlpatterns = [
    path('', views.showformdata),
]
