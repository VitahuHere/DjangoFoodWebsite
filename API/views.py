from django.http import JsonResponse
from django.forms.models import model_to_dict
from accounts.models import Person


def account_data(request, pk):
    obj = Person.objects.get(id=pk)
    r = model_to_dict(obj)
    return JsonResponse(r)


def account_food(request):
    return JsonResponse({'name': 'fuck'})
