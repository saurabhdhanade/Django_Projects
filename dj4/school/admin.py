from django.contrib import admin
from school.models import Exam
from school.models import Contact
from django.contrib.admin.options import ModelAdmin

# Register your models here.
class ExamAdmin(ModelAdmin):
    list_display=['subject','center','rollnum','examdate']
    search_fields=['name','subject','center','rollnum']
    list_filter=['examdate']
    

admin.site.register(Exam,ExamAdmin)


# class ContactAdmin(ModelAdmin):

admin.site.register(Contact)

    
