from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsSuperUserOrStaffReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and \
            request.user.is_authenticated and \
                request.user.is_staff:
            return True
        return request.user.is_authenticated and \
            request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS and \
            request.user.is_authenticated and \
                request.user.is_staff:
            return True
        return request.user.is_authenticated and \
            request.user.is_superuser