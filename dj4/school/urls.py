
from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('exam/',views.ExamListView.as_view()),
    path('exam/<int:pk>',views.ExamDetailView.as_view()),
    path('',RedirectView.as_view(url='exam/')),
    path('about/',views.about),
    path('contact/',views.contact),
]
