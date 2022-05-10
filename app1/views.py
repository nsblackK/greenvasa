from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def buy(request):
    return render(request, 'productPage.html');
def login(request):
    return render(request, 'login_page.html');
def sell(request):
    return render(request, 'sales_page.html');
def description(request):
    return render(request, 'new_product_desc.html');