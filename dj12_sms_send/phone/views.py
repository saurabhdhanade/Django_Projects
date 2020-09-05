from django.shortcuts import render
from .models import SendSMS
from django.http.response import HttpResponse
# Create your views here.
from .smssend import smssend

def index(request):
    if request.method == 'POST':
        sendsms=SendSMS()
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        
        sendsms.name=name
        sendsms.phone=phone
        
            
        sendsms.save()
        
        
        
        
        smssend(phone, 'Hello World')
        
        return HttpResponse('Thank you')
        
        
    return render(request, 'index.html')
