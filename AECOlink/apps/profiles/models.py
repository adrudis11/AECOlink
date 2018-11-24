from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)

class Client(User):
    asdf = models.CharField(max_length=50)
