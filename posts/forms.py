from django import forms
from .models import Post, Tag
from django.contrib.admin import widgets

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=widgets.FilteredSelectMultiple('Tags', is_stacked=False)
    )
    class Meta:
        model = Post
        fields = '__all__'