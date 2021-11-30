from django.db import models
from accounts.models import Person


class Keys(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    client_id = models.CharField(max_length=100)
    client_secret = models.CharField(max_length=100)
