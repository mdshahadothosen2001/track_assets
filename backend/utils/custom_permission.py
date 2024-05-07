from rest_framework.permissions import BasePermission

from utils.utils import tokenValidation


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        payload = tokenValidation(request)
        if payload["is_staff"] is True:
            return True
        else:
            False


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        payload = tokenValidation(request)
        if payload["is_employee"] is True:
            return True
        else:
            False
