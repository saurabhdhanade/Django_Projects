from django.contrib import admin
from university.models import Register
from django.contrib.admin.options import ModelAdmin
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class RegisterAdmin(ImportExportModelAdmin):
#     list_display=['name,','email','dob']
    search_fields=['name']
    list_filter=['dob']


admin.site.register(Register,RegisterAdmin)
