from email import utils
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from internshiptask import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage,send_mail
from . tokens import generate_token
from .models import Plate

# Create your views here.
def home(request):
    if request.method=="POST":
        idplate=request.POST.get('idplate')           
        plateNo=request.POST.get('plateNo')
        phoneNo=request.POST.get('phoneNo')
        plate=Plate(idplate=idplate,plateNo=plateNo,phoneNo=phoneNo)
        plate.save()
    return render(request,'authentication/home.html')

def show(request):
    stud=Plate.objects.all()
    return render(request,'authentication/showRecords.html',{'stu':stud})

def sign(request):
    if request.method=='POST':
        loginusername=request.POST.get('loginusername')
        loginpassword=request.POST.get('loginpassword')
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            return render(request,'authentication/home.html',{'loginusername':loginusername})
        else:
            return redirect("sign")
    return render(request,'authentication/signIn.html')

def signOut(request):   
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('home')

def search(request):
    query=request.GET['query']
    plateID=Plate.objects.filter(idplate__icontains=query)
    plateNumber=Plate.objects.filter(plateNo__icontains=query)
    PhoneNo=Plate.objects.filter(phoneNo__icontains=query)

    stud=plateID | plateNumber | PhoneNo
    # print(stud)
    params={'stu':stud}
    return render(request,'authentication/search.html',params)

def update_data(request,id):
    obj = Plate.objects.get(pk=id)
    if request.method=='POST':
        pi=Plate.objects.get(pk=id)
        pi.idplate=request.POST.get('idplate')
        pi.plateNo=request.POST.get('plateNo')
        pi.phoneNo=request.POST.get('phoneNo')
        pi.save()
    return render(request,'authentication/update.html',{'obj':obj})
