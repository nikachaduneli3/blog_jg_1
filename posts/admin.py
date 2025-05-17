from django.contrib import admin
from .models import Post, Comment, Tag
from .forms import PostForm

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish_date', 'likes', 'dislikes']
    search_fields = ['title', 'content', 'author__username']
    form = PostForm

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'likes', 'dislikes', 'parent_comment']
    search_fields = ['content', 'author__username']


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    search_fields = ['name']
