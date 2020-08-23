from django.shortcuts import render
from water.models import Register 
from django.http.response import HttpResponse
# Create your views here.

def index(request):
    if request.method=="POST":
        register=Register()
        name=request.POST.get('name')
#         email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        designation=request.POST.get('designation')
        adhar=request.POST.get('adhar')
        register.name=name
#         register.email=email
        register.phone=phone
        register.address=address
        register.designation=designation
        register.adhar=adhar
        register.save()
        return render(request, "exit.html")
    
    return render(request, 'index.html')
