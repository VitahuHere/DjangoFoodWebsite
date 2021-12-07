import random
import string

from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

from API.models import Keys
from accounts.models import Person
from accounts.views import encrypt_sha256


def generate_api_keys(client: str):
    """
    Method generating api keys returning dictionary of Keys
    'person': 'example',
    'client_id': 'client id',
    'client_secret': 'client secret'
    :param client:
    :return:
    """
    try:
        return model_to_dict(Keys.objects.get(person_id=client))
    except ObjectDoesNotExist:
        letters = string.ascii_lowercase
        Keys.objects.create(
            person_id=client,
            client_id=encrypt_sha256(''.join(random.choice(letters) for _ in range(10))),
            client_secret=encrypt_sha256(client + ''.join(random.choice(letters) for _ in range(10))),
        )
        return model_to_dict(Keys.objects.get(person_id=client))


def get_request_api_key(request):
    """
    End point to generate api keys, uses 'generate_api_keys' method
    Fetch from request encrypted 'login'
    :param request:
    :return:
    """
    try:
        login = request.GET.get('login')
        response = generate_api_keys(login)
        return JsonResponse(response)
    except KeyError:
        return HttpResponse(status=400)


def get_account_data(request):
    """
    Endpoint to return json dictionary with account information including
    Encrypted login and password
    Else return status 400
    :param request:
    :return:
    """
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
            return HttpResponse(status=401)
    except (ObjectDoesNotExist, KeyError):
        return JsonResponse("account does not exist")
