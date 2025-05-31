from rest_framework import serializers
from unicodedata import category

from .models import Post, Tag, Category
from django.contrib.auth import get_user_model

class PostListSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField(read_only=True, source='author')
    author = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(),
                                            write_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'publish_date', 'author_name', 'author']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PostDetailSerializer(PostListSerializer):
    tags_info = TagSerializer(many=True, source='tags', read_only=True)
    categories_info = CategorySerializer(many=True, source='categories', read_only=True)

    tags = serializers.MultipleChoiceField(choices=Tag.objects.all(), write_only=True)
    categories = serializers.MultipleChoiceField(choices=Category.objects.all(), write_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'publish_date',
                  'author_name', 'author', 'likes', 'dislikes',
                  'content','views', 'tags', 'categories',
                  'tags_info', 'categories_info']
