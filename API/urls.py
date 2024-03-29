from django.urls import path

from . import views

urlpatterns = [
    path('api/obtain-auth-token/', views.obtain_auth_token, name='obtain-auth-token'),
    path('api/get-account-data/', views.get_account_data, name='get-account-data'),
    path('api/create-package/', views.create_package, name='create-package'),
    path('api/check-package-status/', views.check_package_status, name='check-package-status'),
    path('api/create-product/', views.create_product, name='create-product'),
]
