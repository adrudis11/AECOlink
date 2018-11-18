from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)

class Client(User):
    asdf = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    image = models.ImageField(upload_to='post_image', null=True)
    create_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    update_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
