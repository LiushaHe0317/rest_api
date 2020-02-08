from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """check if user has permission to edit the profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

