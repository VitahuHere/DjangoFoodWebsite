from django.http import JsonResponse


def account_data(request):
    payload = {'fuck': 'off'}
    return JsonResponse(payload)


def account_food(request):
    return JsonResponse({'name': 'fuck'})
