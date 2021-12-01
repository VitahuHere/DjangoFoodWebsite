from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('API.urls')),
    path('', include('accounts.urls')),
    path('', include('index.urls')),
    path('admin/', admin.site.urls),
]
