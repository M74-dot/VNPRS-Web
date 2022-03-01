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
from .models import Student

# Create your views here.
def home(request):
    if request.method=="POST":
        student_name=request.POST.get('studentName')
        college_name=request.POST.get('collegeName')
        Specialisation=request.POST.get('specialisation')
        degree=request.POST.get('degree')
        internship=request.POST.get('internship')
        phoneNo=request.POST.get('phoneNo')
        email=request.POST.get('email')
        location=request.POST.get('location')
        gender=request.POST.get('gender')
        notes=request.POST.get('note')
        student=Student(student_name=student_name,college_name=college_name,Specialisation=Specialisation,degree=degree,internship=internship,phoneNo=phoneNo,email=email,location=location,gender=gender,notes=notes)
        student.save()
    return render(request,'authentication/home.html')

def signUp(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if User.objects.filter(username=username):
            messages.error('User already exists!!')
            return redirect('sign')
        
        if User.objects.filter(email=email):
            messages.error('User already exists!!')
            return redirect('sign')


        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,"Account Created Successfully")

        # Welcome Email
        subject='Welcome to Authentication System'
        message="Hello "+myuser.username+ "!!\n" + "Welcome to Authentication System!!\nThank you for visiting our website\nWe have also sent you a confirmation email, Please confirm your Email address in order to activate your account\n\nThanking You\nSayali Katkar"

        from_email=settings.EMAIL_HOST_USER
        to_list=[myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)


        # Confirm Email
        current_site=get_current_site(request)
        email_subject="Confirm Your Email @authentication"
        message2=render_to_string('email_confirmation.html',{
            'name':myuser.username,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token':generate_token.make_token(myuser)
        })
        email=EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email]
        )
        email.fail_silently=True
        email.send()

        return redirect('sign')

    else:
        return render(request,"authentication/signUp.html")


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


def show(request):
    stud=Student.objects.all()
    return render(request,'authentication/showRecords.html',{'stu':stud})

def update_data(request,id):
    obj = Student.objects.get(pk=id)
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        pi.student_name=request.POST.get('studentName')
        pi.college_name=request.POST.get('collegeName')
        pi.Specialisation=request.POST.get('specialisation')
        pi.degree=request.POST.get('degree')
        pi.internship=request.POST.get('internship')
        pi.phoneNo=request.POST.get('phoneNo')
        pi.email=request.POST.get('email')
        pi.location=request.POST.get('location')
        pi.gender=request.POST.get('gender')
        pi.notes=request.POST.get('note')
        pi.save()
    return render(request,'authentication/update.html',{'obj':obj})