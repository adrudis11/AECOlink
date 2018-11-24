from django.db import models
from AECOlink.apps.profiles.models import Client

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    body = models.TextField()
    image = models.ImageField(upload_to='post_image', null=True)
    create_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    update_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)


