# Generated by Django 3.0.5 on 2021-01-13 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Friends', '0011_auto_20201208_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slambook',
            name='slam_no',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]