import email
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from .models import Register
# Create your views here.
############################index#####
def index(request):
  return render(request,'landing_page.html')

def login(request):
    if request.method == 'POST':
        print('Request is made..........')
        Email = request.POST.get('email')  
        Password = request.POST.get('pswd')  
        print(Email)

        try:
          user= Register.objects.get(Email=Email,pwd=Password)
          if user is not None:
            print("user exists")
            return render(request,'sales_page.html')
        except Exception as identifier:
          print("user does not exist")
    #     form = AuthenticationForm(request, request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('email')
    #         password = form.cleaned_data.get('pswd')
    #         print("Username" , username)
    #         print("Password" , password)
    #         user = authenticate(username=username, password=password)
    #         if user is not None:
    #           login(request, user)
    #           return redirect('login:buy')
            
    #         else:
    #             messages.info(request, 'Invalid username or password')
    #     else:
    #         messages.info(request, 'Invalid username or password')
    # form = AuthenticationForm()
    return render(request, 'login_page.html')






    #return render(request,'login_page.html')

def buy(request):
  return render(request,'productPage.html')

############# registerr###
def register(request):
  if request.method== "POST":
    # form=UserRegisterForm(request.POST)
    # if form.is_valid():
    user=2
    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    email=request.POST.get('email')
    phno=request.POST.get('phno')
    pwd=request.POST.get('pswd')
    cpwd=request.POST.get('pswd2')
    register=Register()
    register.user_id=user
    register.firstname=fname
    register.lastname=lname
    register.Email=email
    register.Phno=phno
    register.pwd=pwd
    register.cpwd=cpwd
    register.save()
    


      
      



  return render(request,'register.html')

def resetpwd(request):
  return render(request,'forgot_password.html')

def changepwd(request):
  return render(request,'change_password.html')


def sell(request):
    return render(request, 'sales_page.html');
def description(request):
    return render(request, 'new_product_desc.html');