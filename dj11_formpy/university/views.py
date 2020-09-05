from django.shortcuts import render
from .forms import FormBranch
from university.models import Register
from django.http.response import HttpResponse

# Create your views here.


def showformdata(request):
    fm=FormBranch()
    if request.method=='POST':
        register=Register()
        name=request.POST.get('name')
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        
        register.name=name
        register.email=email
        register.dob=dob
        register.save()
        
        
        return HttpResponse("Thank you")
    
    return render(request,'home.html',{'form':fm})



