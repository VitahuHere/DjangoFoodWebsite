from django.shortcuts import render


def index(request):
    return render(request, 'menu/index.html')


def about(request):
    return render(request, 'menu/about.html')
