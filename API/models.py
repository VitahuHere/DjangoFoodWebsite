import binascii
import os

from rest_framework.authtoken.models import Token
from django.db import models
from accounts.models import Account


class AccountToken(Token):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.key = binascii.hexlify(os.urandom(20)).decode()
