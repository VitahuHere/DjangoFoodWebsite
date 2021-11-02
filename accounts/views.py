from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    return render(request, 'accounts/register.html')


def post_new_account(request):
    print(request.POST)
    return HttpResponse(request)
