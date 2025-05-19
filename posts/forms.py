from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    # tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
    #                                       widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Post
        fields = '__all__'