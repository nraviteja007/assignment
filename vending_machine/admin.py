from django.contrib import admin
from .models import Departments,Doctors


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['serial_no','first_name','last_name','department']

admin.site.register(Departments)
admin.site.register(Doctors,DoctorAdmin)
