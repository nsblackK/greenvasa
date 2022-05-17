from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'landing_page.html')


def login(request):
    return render(request, 'login_page.html')


def buy(request):
    return render(request, 'productPage.html')


def register(request):
    return render(request, 'register.html')


def resetpwd(request):
    return render(request, 'forgot_password.html')


def changepwd(request):
    return render(request, 'change_password.html')


def sell(request):
    print('View is requested')
    if request.method == 'GET':
        print('Get is wirking')
        return render(request,  'sales_page.html')
    elif request.method == 'POST':
        print('View Requested')
      
        return redirect('sell')
    return render(request,  'sales_page.html')

def description(request):
    return render(request, 'new_product_desc.html')
