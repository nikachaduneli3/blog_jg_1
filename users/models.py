from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.PositiveIntegerField(default=18)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=1,
                              choices={
                                  'm': 'Male',
                                  'f': 'Female'
                              })
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='users', default='users/default-user.png')
