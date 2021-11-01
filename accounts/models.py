from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
    weight = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1)])
    height = models.PositiveIntegerField(validators=[MaxValueValidator(999), MinValueValidator(1)])
