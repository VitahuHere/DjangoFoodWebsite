from django.db import models
from django.core.validators import MinValueValidator
from django_better_admin_arrayfield.models.fields import ArrayField
from accounts.models import Account


class Package(models.Model):
    client = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=False)
    title = models.CharField(max_length=100, null=True)
    contents = ArrayField(
        models.CharField(max_length=100, blank=True),
        blank=False,
        null=False,
    )


class Product(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    net_weight = models.FloatField(validators=[MinValueValidator(0)])
    is_liquid = models.BooleanField(default=False)
    allergens = ArrayField(
        models.CharField(max_length=100, blank=True),
        blank=True,
        null=True,
    )
