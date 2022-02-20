from django.urls import path

from . import views

urlpatterns = [
    path('api/obtain-auth-token/', views.obtain_auth_token, name='obtain-auth-token'),
    path('api/get-account-data/', views.get_account_data, name='get-account-data'),
]
