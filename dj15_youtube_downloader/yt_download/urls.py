from django.conf.urls import url

from . import views
from django.urls.conf import path

urlpatterns = [
    url(r'^$',views.greetings),
    url(r'^home/download/$',views.download),
    url(r'home/downloading/$',views.downloading),
]