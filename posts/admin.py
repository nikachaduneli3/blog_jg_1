from django.contrib import admin
from django.urls import reverse
from .models import Post, Comment, Tag, Category
from .forms import PostForm
from django.utils.html import format_html

admin.site.enable_nav_sidebar = False

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['display_image_thumbnail', 'title_link',
                    'categories_formated', 'tags_formated',
                    'author', 'publish_date', 'likes', 'dislikes']
    search_fields = ['title', 'content', 'author__username']
    readonly_fields = ['display_image']
    form = PostForm

    def display_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width=300 height=300/>')

    def display_image_thumbnail(self, obj):
        return format_html(f'<img src="{obj.image.url}" width=100 height=100/>')

    def title_link(self, obj):
        link = reverse("admin:posts_post_change", args=[obj.id])
        return format_html('<a href="{}">{}</a>', link, obj.title)

    def tags_formated(self, obj):
        res = ''
        for tag in obj.tags.all():
           res += f'''<span  style="border-radius: 20px; 
                                    background-color: {tag.color}; 
                                    text-align: center; 
                                    margin: 5px;
                                    padding: 5px;
                                    color: purple">{tag.name}</span>'''
        return format_html(res)

    def categories_formated(self, obj):
        res = ''
        for category in obj.categories.all():
           res += f'''<span  style="border-radius: 20px; 
                                    background-color: #9c0e1c; 
                                    text-align: center; 
                                    margin: 5px;
                                    padding: 5px;
                                    color: white">{category.name}</span>'''
        return format_html(res)

    categories_formated.short_description = 'categories'
    tags_formated.short_description = 'tags'
    title_link.short_description = 'title'
    display_image_thumbnail.short_description = 'thumbnail'


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'post_link', 'likes', 'dislikes', 'parent_comment_link']
    search_fields = ['content', 'author__username']

    def post_link(self, obj):
        link = reverse("admin:posts_post_change", args=[obj.post.id])
        return format_html('<a href="{}">{}</a>', link, obj.post.title)

    def parent_comment_link(self, obj):
        if obj.parent_comment:
            link = reverse("admin:posts_comment_change", args=[obj.parent_comment.id])
            return format_html('<a href="{}">{}</a>', link, obj.parent_comment)
        return  ''

@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_category']
    search_fields = ['name']