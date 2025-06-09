from rest_framework import serializers
from .models import Post, Tag, Category, Comment


class PostListSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField(read_only=True, source='author')
    content = serializers.CharField(write_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'publish_date', 'author_name', 'content']
        read_only_fields = ['publish_date']

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

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField(read_only=True, source='author')
    likes = serializers.IntegerField(read_only=True)
    dislikes = serializers.IntegerField(read_only=True)
    publish_date = serializers.DateTimeField(read_only=True)
    parent_comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), write_only=True, allow_null=True)
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'author_name', 'content', 'parent_comment',
                  'likes', 'dislikes', 'publish_date', 'replies']
    def get_replies(self, obj):
        return CommentSerializer(obj.replies, many=True).data
