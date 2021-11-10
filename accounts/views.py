import hashlib

from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm
from accounts.models import PersonForm, Person


def register(request):
    return render(request, 'accounts/register.html', {'form': RegisterForm})


def post_new_account(request):
    login = hashlib.sha256(request.POST['login'].encode()).hexdigest()
    if request.method == 'POST':
        if Person.objects.filter(pk=login).exists():
            return render(request, 'accounts/redirect_register.html')
        else:
            p = PersonForm(request.POST)
            new = p.save(commit=False)
            new.password = hashlib.sha256(request.POST['password'].encode()).hexdigest()
            new.login = login
            new.save()
            p.save_m2m()
    return redirect('/account/')


def account(request):
    return HttpResponse("nothing here")
