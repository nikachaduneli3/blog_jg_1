from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

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

class FollowRequest(models.Model):
    sent_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_requests')
    sent_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests_to_follow')

    def clean(self, *args, **kwargs):
        if (FollowRequest.
                objects.filter(sent_to=self.sent_to,
                               sent_from=self.sent_from).
                exists()):
            raise ValidationError('This request already exists !')
        if self.sent_to == self.sent_from:
            raise ValidationError('Sender receiver can\'t be same !')
        return super().clean(*args, **kwargs)

    def accept(self):
        self.sent_to.followers.add(self.sent_from)
        self.delete()

    def follow_back(self):
        self.sent_to.followers.add(self.sent_from)
        self.sent_to.following.add(self.sent_from)
        self.delete()

    def reject(self):
        self.delete()
