
from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['username','first_name','last_name','Email','image','contact','password','address']
