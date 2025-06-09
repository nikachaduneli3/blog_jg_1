from django.db import models
from datetime import datetime
from django.conf import settings
from .validators import (
    validate_for_restricted_symbols,
    validate_for_restricted_words,
    validate_future_time

)
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=255, validators=[validate_for_restricted_symbols,
                                                         validate_for_restricted_words])
    publish_date = models.DateTimeField(default=timezone.now, validators=[validate_future_time])
    content = models.TextField(validators=[validate_for_restricted_words])
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='posts/')
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField("Tag", related_name='posts', blank=True)
    categories = models.ManyToManyField('Category', related_name='posts')



    def __str__(self): return self.title

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(validators=[validate_for_restricted_words])
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    publish_date = models.DateTimeField(default=datetime.now)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,
                                       related_name='replies')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self): return f'{self.content[:10]} - {self.author}'


class Tag(models.Model):
    name = models.CharField(max_length=100, validators=[validate_for_restricted_words,
                                                        validate_for_restricted_symbols])
    color = models.CharField(max_length=10, default = 'white',
                             choices={'green': 'Green',
                                      'purple': 'Purple',
                                      'red': 'Red',
                                      'blue': "Blue",
                                      'orange': 'Orange',
                                      'gray': 'Gray',
                                      'white': 'White'})

    def __str__(self): return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', null=True, blank=True,
                                         related_name='subcategories',on_delete=models.CASCADE)

    class Meta:
         verbose_name_plural = 'categories'

    def __str__(self): return self.name
