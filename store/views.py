from django.shortcuts import render
from .models import Product


def hello(request):
    products = Product.objects.filter(last_update__year__lt=2023);
    return render(request,'hello.html',{'products': list(products)})