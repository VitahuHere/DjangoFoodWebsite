from rest_framework.serializers import ModelSerializer
from accounts.models import Account


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['name', 'surname', 'birthday']
        read_only_fields = ['__all__']