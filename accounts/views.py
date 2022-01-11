import hashlib

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from accounts.models import PersonForm, Person, LoggingForm
from .forms import RegisterForm, LoginForm
from packages.models import Package, Products


def account(request):
    """
    After successful register or login, takes cookie 'login' and renders 'account.html' with
    package history.
    :param request:
    :return:
    """
    try:
        login = request.COOKIES.get('login')
        try:
            context = {
                'client': Person.objects.get(login=login),
                'packages': Package.objects.filter(client=login).values(),
            }
            return render(request, 'accounts/account.html', context=context)
        except ObjectDoesNotExist:
            return render(request, 'accounts/account not existing.html')
    except KeyError:
        return render(request, 'accounts/account not existing.html')


def encrypt_sha256(string: str) -> str:
    """
    Method for encrypting strings with sha256
    :param string:
    :return:
    """
    return hashlib.sha256(string.encode()).hexdigest()


def logging_in(request):
    """
    Renders login.html with loginForm from accounts. forms
    :param request:
    :return:
    """
    try:
        Person.objects.get(login=request.COOKIES.get('login'))
        return redirect('/account/')
    except (KeyError, ObjectDoesNotExist):
        return render(request, 'accounts/login.html', {'form': LoginForm})


def post_account_login(request):
    """
    View for checking login request
    Try except catches KeyError if the is no 'login' key
    If login is successful, cookie 'login' set to encrypted 'login'
    Then redirects to 'account/'
    :param request:
    :return:
    """
    if LoggingForm(request.POST).is_valid():
        try:
            login = encrypt_sha256(request.POST['login'])
            if request.method == 'POST':
                if Person.objects.filter(pk=login).exists():
                    password = encrypt_sha256(request.POST['password'])
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


def post_register_account(request):
    """
    View for registering new accounts
    Takes data from request
    Try except for catching not existing db record or not existing 'login' key
    Value from request 'login' is encrypted with sha256
    Checks if login already exists and returns 'redirect existing login.html'
    Else checks if form is valid and creates new record to Person model
    And redirects to 'account/' url
    :param request:
    :return:
    """

    try:
        login = encrypt_sha256(request.POST['login'])
        if request.method == 'POST':
            if Person.objects.filter(pk=login).exists():
                return render(request, 'accounts/redirect existing login.html')
            p = PersonForm(request.POST)
            if p.is_valid():
                new = p.save(commit=False)
                new.password = encrypt_sha256(request.POST['password'])
                new.login = login
                new.save()
                p.save_m2m()
                r = redirect('/account/')
                r.set_cookie('login', login)
                return r
            else:
                return render(request, 'accounts/redirect invalid form.html')
    except (ObjectDoesNotExist, KeyError):
        return render(request, 'accounts/redirect invalid form.html')


def register(request):
    """
    Renders 'register.html' with RegisterForm from accounts.form
    :param request:
    :return:
    """
    return render(request, 'accounts/register.html', {'form': RegisterForm})
