import hashlib

from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

from API.models import Keys
from accounts.models import Person, PersonForm
from accounts.views import encode_sha256


def generate_api_keys(who: str):
    client = encode_sha256(who)
    try:
        return JsonResponse(model_to_dict(Keys.objects.get(client_id=client)))
    except ObjectDoesNotExist:
        Keys.objects.create(client_id=client, client_secret=encode_sha256(client), person_id=who)
        return JsonResponse(model_to_dict(Keys.objects.get(client_id=client)))


def get_request_api_key(request):
    login = request.GET.get('login')
    response = generate_api_keys(login)
    return HttpResponse(response)


def get_account_data(request):
    try:
        obj = Person.objects.get(login=request.GET.get('login'))
        r = model_to_dict(obj)
        return JsonResponse(r)
    except ObjectDoesNotExist:
        return HttpResponse("account does not exist")


def post_new_person(request):
    login = hashlib.sha256(request.POST['login'].encode()).hexdigest()
    if request.method == 'POST':
        if Person.objects.filter(pk=login).exists():
            return HttpResponse("account already exists")
        p = PersonForm(request.POST)
        if p.is_valid():
            new = p.save(commit=False)
            new.password = hashlib.sha256(request.POST['password'].encode()).hexdigest()
            new.login = login
            new.save()
            p.save_m2m()
        return HttpResponse(status=204)
