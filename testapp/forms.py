from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'sex',
        )
        widgets = {
            'sex': forms.ChoiceField(choices=Post.USER_TYPE)
        }
