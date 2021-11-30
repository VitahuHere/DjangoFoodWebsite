from django.urls import path
from . import views

urlpatterns = [
    path('api/get/account/data/', views.get_account_data, name='get_account_data'),
    path('api/post/account/', views.post_new_person, name='post_new_person'),
]
