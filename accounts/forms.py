from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class RegisterForm(forms.Form):
    login = forms.CharField(label='Your login:', max_length=100)
    password = forms.CharField(label='Your Password:', max_length=100, widget=forms.PasswordInput())
    name = forms.CharField(label='Your name:', max_length=100)
    surname = forms.CharField(label='Your surname', max_length=100)
    birthday = forms.DateField(label='Your birthday', widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    weight = forms.DecimalField(label='Your weight:', max_digits=5, decimal_places=1, validators=[MinValueValidator(1)])
    height = forms.IntegerField(label='Your height:', validators=[MinValueValidator(1), MaxValueValidator(999)])


class LoginForm(forms.Form):
    login = forms.CharField(label='Your login:', max_length=100)
    password = forms.CharField(label='Your Password:', max_length=100, widget=forms.PasswordInput())