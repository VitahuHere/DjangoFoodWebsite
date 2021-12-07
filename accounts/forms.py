from django import forms


class LoginForm(forms.Form):
    """
    Login form for rendering in 'login.html'
    """
    login = forms.CharField(label='Your login:', max_length=100)
    password = forms.CharField(label='Your Password:', max_length=100, widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    """
    Register form for rendering in template 'register.html'
    """
    login = forms.CharField(label='Your login:', max_length=100)
    password = forms.CharField(label='Your Password:', max_length=100, widget=forms.PasswordInput())
    name = forms.CharField(label='Your name:', max_length=100)
    surname = forms.CharField(label='Your surname', max_length=100)
    birthday = forms.DateField(label='Your birthday', widget=forms.widgets.DateInput(attrs={'type': 'date'}))

