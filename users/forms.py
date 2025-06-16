from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.models import Group, Permission
from .models import User


class UserForm(UserChangeForm):
    user_permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=widgets.FilteredSelectMultiple('Permissions',
                                              is_stacked=False),
        required = False
    )

    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=widgets.FilteredSelectMultiple('Groups', is_stacked=False),
        required=False

    )

    class Meta:
        model = User
        fields = '__all__'
