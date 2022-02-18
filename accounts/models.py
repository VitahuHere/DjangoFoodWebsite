from hashlib import sha256

from django.db import models
from django.forms import ModelForm


class Account(models.Model):
    login = models.CharField(max_length=100, primary_key=True, default=None, unique=True)
    password = models.CharField(max_length=200, default=None)
    name = models.CharField(max_length=100, default=None)
    surname = models.CharField(max_length=100, default=None)
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(blank=False, max_length=100, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.login = sha256(self.login.encode()).hexdigest()
        self.password = sha256(self.password.encode()).hexdigest()
        super().save()


class PersonForm(ModelForm):
    """
    Form to validate sent form for registration
    """
    class Meta:
        model = Account
        fields = ['login', 'password', 'name', 'surname', 'birthday']


class LoggingForm(ModelForm):
    """
    Form to validate login form
    """
    class Meta:
        model = Account
        fields = ['login', 'password']
