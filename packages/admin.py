from django.contrib import admin
from .models import Package, Product, Status
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin, DynamicArrayMixin):
    ...


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin, DynamicArrayMixin):
    ...


admin.site.register(Status)
