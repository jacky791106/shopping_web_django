from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register(request):
    return render(request,'register.html')

def register_check(request):
    account = request.POST.get('account')
    password = request.POST.get('password')
    check_password = request.POST.get('check_password')
    name = request.POST.get('name')
    tel = request.POST.get('tel')
    email = request.POST.get('email')
    address = request.POST.get('address')

    data={}
    data['username']=account
    data['password']=password
    return render(request,'register_check.html',data)
