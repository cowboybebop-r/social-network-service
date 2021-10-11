from rest_framework import permissions


class IsPostOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, post):
        if request.method in permissions.SAFE_METHODS:
            return True
        return post.user == request.user
