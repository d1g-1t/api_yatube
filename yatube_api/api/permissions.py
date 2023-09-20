from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешения позволяют редактировать записи только их авторам.
    Для остальных пользователей - только чтение.
    """
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
