from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)  # textfield Unrestricted text
    date_posted = models.DateTimeField(default=timezone.now)  # No parenthesis so function isn't executed but passed in
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # If user is deleted, all posts are deleted with CAS
