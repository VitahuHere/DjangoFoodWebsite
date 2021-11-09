from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Person(models.Model):
    login = models.CharField(max_length=100, primary_key=True, default=None)
    password = models.CharField(max_length=200, default=None)
    name = models.CharField(max_length=100, default=None)
    surname = models.CharField(max_length=100, default=None)
    birthday = models.DateField(null=False, default=None)
    weight = models.DecimalField(max_digits=5, decimal_places=1, validators=[MinValueValidator(1)], default=None)
    height = models.PositiveIntegerField(validators=[MaxValueValidator(999), MinValueValidator(1)], default=None)