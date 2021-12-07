from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('API.urls')),
    path('', include('accounts.urls')),
    path('', include('index.urls')),
    path('', include('packages.urls')),
    path('', include('recipes.urls')),
    path('admin/', admin.site.urls),
]
