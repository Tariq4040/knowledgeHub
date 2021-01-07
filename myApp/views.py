from django.shortcuts import render , HttpResponse
from myApp.models import Contact1
from myApp.models import Personal_Contact_Form
import datetime
from django.contrib import messages


var={
    "info":"this is me and myself is M.Tariq Ahmad, and   we live in sahiwal",
    "name":"tariq ahmad",
    "age"   :25
    }
# python page ka content or data hm yahan pe dictionarybna k html page pe bhaj skte h.....like below,neche success message b hm esi rule se base.html page pe bhaj rhe h.....
    # return render(request , 'index.html',var) yahan pe var dictionary name h or os andr content majood h,
    # es content mtlb keys ko index.html page me use kr skte h,or ose hm odr design kr skte h.....try yourself 

def index(request):
    # ye sare k sare messge h jinhe opr hm ne import kea hwa h.....meesage ko.....enhe hm different purpose  lea k use kr skte h like,welcome message on page,info message,error message and also db debug and success message.
    # messages.warning(request, 'Are you sure ....Vist My website....')
    # messages.info(request, 'this is Innformation Tab....')
    # messages.error(request, 'Error Message is Flashed....')
    # messages.debug(request, 'Debug Message....')

    return render(request , 'index.html')
    # return HttpResponse("this is M.Tariq Ahmad and this is Home Page")

def skill(request):
    return render(request , 'skill.html')

def contact(request):
    if request.method=='POST':
        name1=request.POST.get('name')
        email1=request.POST.get('email')
        address1=request.POST.get('adrs')
        city1=request.POST.get('city')
        zip1=request.POST.get('zip')
        desc1=request.POST.get('disc')

        store1=Contact1(name=name1 , email=email1 , address=address1 , city=city1 , zip=zip1 , disc=desc1 , date=datetime.date.today())
        store1.save()
        messages.success(request, 'Your Data Has Been Succesfully Sent')


    return render(request , 'contact.html')

def service(request):
    return render(request , 'service.html') 

def personal_contactForm(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('pNo')
    #     country=request.POST.get('country')
    #     state=request.POST.get('state')
        var=Personal_Contact_Form(name=name , phone_no=phone)
        var.save()

        messages.success(request, 'Your Data Has Been Succesfully Sent')

    return render(request ,'personal_contactForm.html')