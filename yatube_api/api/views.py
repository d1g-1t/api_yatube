from rest_framework import permissions, viewsets
from django.shortcuts import get_object_or_404

from posts.models import Group, Post
from api.permissions import AuthorOrReadOnly
from api.serializers import GroupSerializer, PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Post."""
    serializer_class = PostSerializer
    queryset = Post.objects.all().select_related('author')
    permission_classes = (
        permissions.IsAuthenticated, AuthorOrReadOnly
    )

    def perform_create(self, serializer):
        """Функция создания нового поста."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели Group."""
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Comment."""
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticated, AuthorOrReadOnly
    )

    def get_queryset(self):
        """Функция получения комментариев к определенному посту."""
        return self.get_post().comments.select_related('author')

    def get_post(self):
        """Функция получения конкретного поста по id."""
        return get_object_or_404(
            Post, pk=self.kwargs.get('post_id')
        )

    def perform_create(self, serializer):
        """Функция создания комментария отдельным автором."""
        serializer.save(
            author=self.request.user,
            post=self.get_post()
        )
