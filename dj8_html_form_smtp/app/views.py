from django.shortcuts import render
from app.models import Members
from django.http.response import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    if request.method == 'POST':
        members=Members()
        name=request.POST.get('name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        address=request.POST.get('address')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        designation=request.POST.get('designation')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        age=request.POST.get('age')
        blood=request.POST.get('blood')
        
        members.name=name
        members.username=username
        members.password=password
        members.address=address
        members.email=email
        members.phone=phone
        members.designation=designation
        members.gender=gender
        members.dob=dob
        members.age=age
        members.blood=blood
        members.save()
        
        send_mail(
        "Warje WTP REgistration form Status",
        'Dear '+name+" \n\nYour form is successfully Registered.\n\nUsername:"+username+ "\n\nPassword:"+password+" \n\n\n\nThanks for Apply",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False)
        
        
        
        
        return HttpResponse("<h1>Thanks for connect us. you will receive User name and Password on your email</h1>")
        
        
    return render(request, 'index.html')
