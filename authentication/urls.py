from django import views
from django.contrib import admin
from django.urls import path
from authentication import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('signUp',views.signUp,name='signUp'),
    path('sign',views.sign,name='sign'),
    path('signOut',views.signOut,name='signOut'),
    path('show',views.show,name='show'),
]