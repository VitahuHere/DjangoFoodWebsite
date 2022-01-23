from django.shortcuts import render
from packages.models import Product


def products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'packages/products.html', context)


def order(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'packages/order.html', context)
