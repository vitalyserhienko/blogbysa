from django.contrib.auth.models import User
from .models import Post, Comment, Profile
from django import forms

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['country', 'city', 'birthday']
        widgets = {
            'birthday': DateInput()
        }

class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            'post_title',
            'post_city',
            'post_country',
            'post_date',
            'post_content',
            'post_photo'
        ]
        widgets = {
            'post_date': DateInput()
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment_text',)
