from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from accounts.models import Person


def get_account_data(request, pk):
    obj = Person.objects.get(login=pk)
    r = model_to_dict(obj)
    return JsonResponse(r)


def post_new_person(request):
    return HttpResponse(request)
