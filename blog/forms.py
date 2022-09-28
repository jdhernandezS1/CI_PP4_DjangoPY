from django import forms
from .models import Comment


class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'body']
