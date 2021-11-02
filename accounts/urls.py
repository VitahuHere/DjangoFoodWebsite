from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('post/register/data/', views.post_new_account, name='post_new_account'),
]
