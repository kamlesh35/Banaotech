from django.contrib import admin
from.models import Doctor,Patient

# Register your models here.

@admin.register(Doctor)
class doctordetails(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','Email','image','contact','password','address')



@admin.register(Patient)
class patientdetails(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','Email','image','contact','password','address')