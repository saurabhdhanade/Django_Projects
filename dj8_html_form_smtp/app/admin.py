from django.contrib import admin
from app.models import Members
from django.contrib.admin.options import ModelAdmin
# Register your models here.

class MembersAdmin(ModelAdmin):
    list_display=['name','address','email']
    search_fields=['name','address','email']
    list_filter=['email']
    



admin.site.register(Members,MembersAdmin)
