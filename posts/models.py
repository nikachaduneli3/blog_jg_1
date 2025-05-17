from django.db import models
from datetime import datetime
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateTimeField(default=datetime.now)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='posts/')
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

    def __str__(self): return self.title

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    publish_date = models.DateTimeField(default=datetime.now)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,
                                       related_name='replies')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self): return f'{self.post.title} - {self.author}'


class Tag(models.Model):
    name = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post, related_name='tags', null=True, blank=True)

    def __str__(self): return self.name


