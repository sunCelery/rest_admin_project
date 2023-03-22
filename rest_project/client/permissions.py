from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `user` attribute.
    """
    def has_object_permission(self, request, view, obj):
        """
        Allow safe methods for everybody.

        Allow other methods when client from db
        is the same client who is doing request.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
