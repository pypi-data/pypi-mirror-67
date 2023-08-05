from rest_framework.permissions import BasePermission


class IsSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return user == obj
