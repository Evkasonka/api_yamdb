from rest_framework import permissions


class IsAuthorOrIsStaff(permissions.BasePermission):
    """Разрешения для автора и выше"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff or obj.author == request.user
