from django.shortcuts import render
from django.contrib.auth.models import *
from.models import *

# Create your views here.

def signup(request):
    if request.method == "POST":
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        e = request.POST['Email']
        con = request.POST['contact']
        im = request.FILES['image']
        add = request.POST['add']
        p = request.POST['pwd'] 
        type = request.POST['type']
        if type=="Doctor":
            Doctor.objects.create(username=uname,password=p,first_name=fname,last_name=lname,contact=con,address=add,image=im,Email=e)
        else:
            Patient.objects.create(username=uname,password=p,first_name=fname,last_name=lname,contact=con,address=add,image=im,Email=e)
    return render(request,'signup.html')



