from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Allow admins full access, others only safe methods (GET, HEAD, OPTIONS).
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsAuthenticatedUser(BasePermission):
    """
    Allow only authenticated users to perform actions.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
