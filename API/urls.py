from django.urls import path

from . import views

urlpatterns = [
    path('api/post/obtain-auth-token/', views.obtain_auth_token, name="obtain-auth-token"),
]
