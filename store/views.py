from django.shortcuts import render
from django.db.models import Q,F
from .models import Product


def hello(request):
    # inventory == price // two fields
    products = Product.objects.filter(
        inventroy=F('unit_price')
    )
    return render(request,'hello.html',{'products': list(products)})