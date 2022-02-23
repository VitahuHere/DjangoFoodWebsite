from .models import AccountToken
from .serializers import AccountSerializer
from .permissions import IsAuthenticated
from accounts.models import Account
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from packages.models import Package


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_package_status(request):
    try:
        login = request.GET['login']
        password = request.GET['password']
        client = Account.objects.get(login=login, password=password)

        try:
            pk = request.GET['id']
            obj = Package.objects.get(pk=pk, client=client)
            return Response({'detail': obj.status.pk}, status=200)
        except KeyError:
            return Response({'detail': 'Missing package id'}, status=403)
        except ObjectDoesNotExist:
            return Response({'detail': 'Package does not exist'}, status=400)

    except KeyError:
        return Response({'detail': 'Missing credentials'}, status=403)
    except ObjectDoesNotExist:
        return Response({'detail': 'Invalid credentials'}, status=403)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_package(request):
    try:
        try:
            login = request.POST['login']
            password = request.POST['password']
            client = Account.objects.get(login=login, password=password)
        except (KeyError, ObjectDoesNotExist):
            return Response({'detail': 'Invalid credentials'}, status=403)
        address = request.POST['address']
        title = request.POST['title']
        contents = request.POST['contents']
        Package.objects.create(client=client,
                               address=address,
                               title=title,
                               contents=contents,
                               )
        return Response({'detail': 'Successfully created package'}, status=200)
    except KeyError:
        return Response({'detail': 'Invalid package details'}, status=403)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_account_data(request):
    try:
        login = request.GET['login']
        password = request.GET['password']
        user = Account.objects.get(login=login, password=password)
        return Response(AccountSerializer(user).data)
    except (KeyError, ObjectDoesNotExist):
        return Response({'detail': 'Invalid credentials'}, status=403)


@api_view(['POST'])
def obtain_auth_token(request):
    try:
        login = request.POST['login']
        password = request.POST['password']
        user = Account.objects.get(login=login, password=password)
        token, created = AccountToken.objects.get_or_create(user=user)
        return Response({'token': token.key})
    except (KeyError, ObjectDoesNotExist):
        return Response({'detail': 'Invalid credentials'}, status=403)