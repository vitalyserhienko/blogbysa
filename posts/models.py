from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.dispatch import receiver
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    birthday = models.DateField(null=True, blank=True)

class Post(models.Model):
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_user')
    post_title = models.CharField(max_length=255)
    post_city = models.CharField(max_length=100)
    post_country = models.CharField(max_length=100)
    post_date = models.DateTimeField()
    post_likes = models.ManyToManyField(User, blank=True, related_name='post_likes')
    post_content = models.TextField(max_length=10000)
    post_photo = models.ImageField(upload_to='post_images/', blank=True)

class Comment(models.Model):
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    comment_post =  models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    comment_text = models.TextField(max_length=10000)
    comment_created_date = models.DateTimeField(default=timezone.now)
