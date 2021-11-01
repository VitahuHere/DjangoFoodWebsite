from django.urls import path
from . import views

urlpatterns = [
    path('API/get/account/data', views.account_data),
    path('API/get/account/food', views.account_food),
]
