from .models import AccountToken
from .serializers import AccountSerializer
from .permissions import IsAuthenticated
from accounts.models import Account
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


@api_view(['POST'])
def obtain_auth_token(request):
    try:
        login = request.POST['login']
        password = request.POST['password']
        user = Account.objects.get(login=login, password=password)
        token, created = AccountToken.objects.get_or_create(user=user)
        return Response({'token': token.key})
    except (KeyError, ObjectDoesNotExist):
        return Response({'detail': 'Invalid credentials'}, status=401)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_account_data(request):
    try:
        login = request.GET['login']
        password = request.GET['password']
        user = Account.objects.get(login=login, password=password)
        return Response(AccountSerializer(user).data)
    except (KeyError, ObjectDoesNotExist):
        return Response({'detail': 'invalid credentials'}, status=403)