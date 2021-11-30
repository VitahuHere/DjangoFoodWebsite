from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from accounts.models import Person
from API.models import Keys
from accounts.views import encode_sha256
from django.core.exceptions import ObjectDoesNotExist


def generate_api_keys(who: str):
    client = encode_sha256(who)
    try:
        Keys.objects.get(client_id=client)
    except ObjectDoesNotExist:
        Keys.objects.create(client_id=client, client_secret=encode_sha256(client), person_id=who)


def


def get_account_data(request):
    obj = Person.objects.get()
    r = model_to_dict(obj)
    return JsonResponse(r)


def post_new_person(request):
    return HttpResponse(request)
