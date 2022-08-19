from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render (request,'index.html')

def product_detail(request):
    return render (request,'product_detail.html')

def cart (request):
    return render (request,'cart.html')

def products(request):
    return render (request,'products.html')

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render (request,'contact.html')

def register(request):
    return render (request,'register.html')