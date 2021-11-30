import hashlib

from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm, LoginForm
from accounts.models import PersonForm, Person, LoggingForm


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
                r = redirect('/account/')
                r.set_cookie('login', login)
                return r
            else:
                return render(request, 'accounts/redirect invalid form.html')


def logging_in(request):
    return render(request, 'accounts/login.html', {'form': LoginForm})


def encode_sha256(string):
    return hashlib.sha256(string.encode()).hexdigest()


def post_account_login(request):
    if LoggingForm(request.POST).is_valid():
        try:
            login = encode_sha256(request.POST['login'])
            if request.method == 'POST':
                if Person.objects.filter(pk=login).exists():
                    password = encode_sha256(request.POST['password'])
                    if Person.objects.get(pk=login).password == password:
                        r = redirect('/account/')
                        r.set_cookie('login', login)
                        return r
                    else:
                        return render(request, 'accounts/account not existing.html')
                else:
                    return render(request, 'accounts/account not existing.html')
        except KeyError:
            return render(request, 'accounts/redirect invalid form.html')


def account(request):
    return HttpResponse("nothing here")
