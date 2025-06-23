from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.PositiveIntegerField(default=18)
    address = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True,
                              choices={
                                  'm': 'Male',
                                  'f': 'Female'
                              })
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='users', default='users/default-user.png')
    following = models.ManyToManyField('self',related_name='followers',
                                       symmetrical=False,)
    is_public = models.BooleanField(default=True)