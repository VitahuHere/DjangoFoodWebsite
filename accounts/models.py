from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.forms import ModelForm


class Person(models.Model):
    login = models.CharField(max_length=100, primary_key=True, default=None, unique=True)
    password = models.CharField(max_length=200, default=None)
    name = models.CharField(max_length=100, default=None)
    surname = models.CharField(max_length=100, default=None)
    birthday = models.DateField(blank=True, null=True)
    weight = models.DecimalField(max_digits=4, decimal_places=1, validators=[MinValueValidator(1)], default=None)
    height = models.PositiveIntegerField(validators=[MaxValueValidator(999), MinValueValidator(1)], default=None)


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['login', 'password', 'name', 'surname', 'birthday', 'weight', 'height']


class LoggingForm(ModelForm):
    class Meta:
        model = Person
        fields = ['login', 'password']
