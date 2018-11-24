from django.db import models

# Create your models here.
class Client(models.Model):
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    foto_perfil = models.ImageField(upload_to='post_image', null=True)
    email = models.EmailField(max_length=254)

class Profesional(models.Model):
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    foto_perfil = models.ImageField(upload_to='post_image', null=True)
    email = models.EmailField(max_length=254)
    empresa = models.CharField(max_length=50)
    localidad = models.TextField(max_length=200)
    fecha_registro = models.DateTimeField()

class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    foto_perfil = models.ImageField(upload_to='post_image', null=True)

