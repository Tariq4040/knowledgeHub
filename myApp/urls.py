from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('' , views.index , name='home'),
    path('skill' , views.skill , name='skill'),
    path('contact' , views.contact , name='contact'),
    path('service' , views.service , name='service'),
    path('personal_contactForm' , views.personal_contactForm , name='personal_contactForm')
]