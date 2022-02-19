import binascii
import os

from django.db import models
from accounts.models import Account


class AccountToken(models.Model):
    key = models.CharField(max_length=40, primary_key=True, )
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = binascii.hexlify(os.urandom(20)).decode()
        return super().save(*args, **kwargs)
