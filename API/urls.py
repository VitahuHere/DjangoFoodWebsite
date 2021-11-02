from django.urls import path
from . import views

urlpatterns = [
    path('api/get/account/data/<int:pk>', views.get_account_data),
    path('api/post/account/', views.post_new_person),
]
