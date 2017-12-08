from django.contrib import admin
from posts.models import Profile, Post, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
