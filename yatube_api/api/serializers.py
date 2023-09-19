from rest_framework import serializers

from posts.models import Post, Comment, Group


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""
    """В сериализацию передаём все поля модели."""
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post."""
    """В сериализацию передаём все поля модели."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""
    """В сериализацию передаём все поля модели."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)
