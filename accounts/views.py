import datetime
import hashlib

from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm
from accounts.models import Person


def register(request):
    return render(request, 'accounts/register.html', {'form': RegisterForm})


def post_new_account(request):
    if request.method == 'POST':
        rq = request.POST
        Person.objects.create(login=rq['login'],
                              name=rq['name'],
                              password=hashlib.sha256(request.POST['password'].encode()).hexdigest(),
                              surname=rq['surname'],
                              birthday=datetime.date(year=int(rq['birthday_year']),
                                                     month=int(rq['birthday_month']),
                                                     day=int(rq['birthday_day'])),
                              weight=rq['weight'],
                              height=rq['height'])
    return HttpResponse(request)
