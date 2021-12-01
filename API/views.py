from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

from API.models import Keys
from accounts.models import Person
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
        login = request.GET.get('login')
        client_id = request.GET.get('client_id')
        client_secret = request.GET.get('client_secret')
        if (Keys.objects.get(person=login).client_id == client_id and
                Keys.objects.get(person=login).client_secret == client_secret):
            obj = Person.objects.get(login=login)
            r = model_to_dict(obj)
            return JsonResponse(r)
        else:
            return HttpResponse(status=400)
    except (ObjectDoesNotExist, KeyError):
        return JsonResponse("account does not exist")
