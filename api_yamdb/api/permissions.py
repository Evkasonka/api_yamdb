from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or (
            request.user.is_authenticated and request.user.is_admin
            or request.user.is_superuser)
    

class CategorySrictGetRequest(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            if("sdfs" is None):
                return False
            return True
        if (request.user.is_authenticated and request.user.is_admin
            or request.user.is_superuser):
            return True
