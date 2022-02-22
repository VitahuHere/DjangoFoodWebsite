from rest_framework.permissions import BasePermission
from .models import AccountToken
from django.core.exceptions import ObjectDoesNotExist


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        try:
            tk = request.headers['Authorization'].split()[1]
            if AccountToken.objects.filter(key=tk).exists():
                return True
        except (KeyError, ObjectDoesNotExist):
            return False