from .models import AccountToken
from accounts.models import Account
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def obtain_auth_token(request):
    try:
        login = request.POST['login']
        password = request.POST['password']
        user = Account.objects.get(login=login, password=password)
        token, created = AccountToken.objects.get_or_create(user=user)
        return Response({'token': f'Token {token.key}'})
    except (KeyError, ObjectDoesNotExist):
        return Response({'detail': 'Invalid credentials'}, status=400)