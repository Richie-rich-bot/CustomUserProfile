from rest_framework import permissions


class OwnProfile(permissions.BasePermission):
    """Allow user to edit theie own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trting to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id