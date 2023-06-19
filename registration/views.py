from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=="POST":
        usn=request.POST.get('usn','')
        name=request.POST.get('name','')
        branch=request.POST.get('branch','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        if usn and name and branch and email:
            contact=Contact(usn=usn,name=name,branch=branch,phone=phone,email=email)
            contact.save()
            return HttpResponse("Details has been successfully created")
           
        else:
            return HttpResponse("enter all the details")


    return render(request,'index.html')