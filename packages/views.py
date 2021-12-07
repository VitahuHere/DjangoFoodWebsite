from django.shortcuts import render
from packages.models import Products


def products(request):
    context = {
        'products': Products.objects.all()
    }
    return render(request, 'packages/products.html', context)

