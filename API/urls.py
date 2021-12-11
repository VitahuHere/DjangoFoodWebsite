from django.urls import path

from . import views

urlpatterns = [
    path('api/get/account/data/', views.get_account_data, name='get_account_data'),
    path('api/get/request_api_key/', views.get_request_api_key, name='get_request_api_key'),
]
