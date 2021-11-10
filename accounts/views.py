import hashlib

from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm, LoginForm
from accounts.models import PersonForm, Person


def register(request):
    return render(request, 'accounts/register.html', {'form': RegisterForm})


def post_register_account(request):
    login = hashlib.sha256(request.POST['login'].encode()).hexdigest()
    if request.method == 'POST':
        if Person.objects.filter(pk=login).exists():
            return render(request, 'accounts/redirect existing login.html')
        else:
            p = PersonForm(request.POST)
            if p.is_valid():
                new = p.save(commit=False)
                new.password = hashlib.sha256(request.POST['password'].encode()).hexdigest()
                new.login = login
                new.save()
                p.save_m2m()
                return redirect('/account/')
            else:
                return render(request, 'accounts/redirect invalid form.html')


def logging_in(request):
    return render(request, 'accounts/login.html', {'form': LoginForm})


def post_account_login(request):
    login = hashlib.sha256(request.POST['login'].encode()).hexdigest()
    if request.method == 'POST':
        if Person.objects.filter(pk=login).exists():
            password = hashlib.sha256(request.POST['password'].encode()).hexdigest()
            if Person.objects.get(pk=login).password == password:
                return redirect('/account/')
            else:
                return render(request, 'accounts/account not existing.html')
        else:
            return render(request, 'accounts/account not existing.html')


def account(request):
    return HttpResponse("nothing here")
