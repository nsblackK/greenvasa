from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context


# Create your views here.
def index(request):
  return render(request,'landing_page.html')

def login(request):
    return render(request,'login_page.html')

def buy(request):
  return render(request,'productPage.html')

def register(request):
  return render(request,'register.html')

def resetpwd(request):
  return render(request,'forgot_password.html')

def changepwd(request):
  return render(request,'change_password.html')


def sell(request):
    return render(request, 'sales_page.html');
def description(request):
    return render(request, 'new_product_desc.html');