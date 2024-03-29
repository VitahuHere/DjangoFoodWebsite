from django.urls import path

from . import views

urlpatterns = [
    path('account/', views.account, name='account'),
    path('login/', views.logging_in, name='login'),
    path('post/register/data/', views.post_register_account, name='post_register_account'),
    path('post/login/data/', views.post_account_login, name='post_account_login'),
    path('register/', views.register, name='register'),
]
