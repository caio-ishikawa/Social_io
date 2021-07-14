from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Comment, Post, Profile

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_content',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_content',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_name', 'profile_bio', 'profile_pic',)
