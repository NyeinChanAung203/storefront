from django.shortcuts import render
from django.db.models import Q
from .models import Product


def hello(request):
    products = Product.objects.filter(
        Q(inventory__lt=10) | Q(unit_price=20)
    );
    products = Product.objects.filter(
        Q(inventory__lt=10) & Q(unit_price=20)
    );
    products = Product.objects.filter(
        Q(inventory__lt=10) & ~Q(unit_price=20)
    );
    # ~ not
    return render(request,'hello.html',{'products': list(products)})