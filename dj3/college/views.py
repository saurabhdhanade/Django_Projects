from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def index(req):
    return render(req, "index.html")

def about(req):
    return render(req, "about.html")

def contact(req):
    return render(req, "contact.html")



