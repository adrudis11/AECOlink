# Generated by Django 2.1.3 on 2018-11-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesionals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('foto_perfil', models.ImageField(null=True, upload_to='post_image')),
                ('email', models.EmailField(max_length=254)),
                ('empresa', models.CharField(max_length=50)),
                ('localidad', models.TextField(max_length=200)),
                ('fecha_registro', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Treballador',
        ),
        migrations.AddField(
            model_name='client',
            name='password',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='password',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
