from django.shortcuts import render
from django.views.generic.list import ListView
from school.models import Exam
from school.models import Contact
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

class ContactDetailView(DetailView):
    model=Contact

# @method_decorator(login_required, name = 'dispatch')
class ExamListView(ListView):
    model=Exam
    
@method_decorator(login_required, name = 'dispatch')    
class ExamDetailView(DetailView):
    model=Exam
