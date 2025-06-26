from django.contrib import admin
from .models import User, FollowRequest
from .forms import UserForm

class FollowersInline(admin.TabularInline):
    model = User.following.through
    fk_name = 'to_user'
    verbose_name = 'follower'
    verbose_name_plural = 'followers'
    extra = 0


class FollowingInline(admin.TabularInline):
    model = User.following.through
    fk_name = 'from_user'
    verbose_name = 'following'
    verbose_name_plural = 'followings'
    extra = 0


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    form = UserForm
    inlines = [FollowersInline, FollowingInline]
    list_display = ['username', 'first_name', 'is_staff', 'is_superuser','is_active']


@admin.register(FollowRequest)
class FollowRequestAdmin(admin.ModelAdmin):
    list_display = ['sent_from', 'sent_to']