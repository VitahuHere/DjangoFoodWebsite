from django.contrib import admin
from .models import Package, Products
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin, DynamicArrayMixin):
    ...


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin, DynamicArrayMixin):
    ...
