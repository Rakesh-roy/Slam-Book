# Generated by Django 3.0.5 on 2020-12-08 08:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Friends', '0009_auto_20201113_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slambook',
            name='user',
        ),
        migrations.AddField(
            model_name='slambook',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
