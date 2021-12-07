from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.forms import ModelForm


class Person(models.Model):
    login = models.CharField(max_length=100, primary_key=True, default=None, unique=True)
    password = models.CharField(max_length=200, default=None)
    name = models.CharField(max_length=100, default=None)
    surname = models.CharField(max_length=100, default=None)
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(blank=False, max_length=100, null=True)


class PersonForm(ModelForm):
    """
    Form to validate sent form for registration
    """
    class Meta:
        model = Person
        fields = ['login', 'password', 'name', 'surname', 'birthday']


class LoggingForm(ModelForm):
    """
    Form to validate login form
    """
    class Meta:
        model = Person
        fields = ['login', 'password']
