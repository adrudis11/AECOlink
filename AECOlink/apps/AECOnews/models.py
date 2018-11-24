from django.db import models
import datetime
from apps.profiles.models import Client

class User(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    body = models.TextField()
    image = models.ImageField(upload_to='post_image', null=True)
    create_at = models.DateTimeField(datetime.datetime, auto_now=True, auto_now_add=False, null=True)
    update_at = models.DateTimeField(datetime.datetime, auto_now=False, auto_now_add=True, null=True)
    crator = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)

