# Generated by Django 3.0.5 on 2020-04-27 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlamBook',
            fields=[
                ('slam_no', models.IntegerField(primary_key=True, serialize=False)),
                ('my_name', models.CharField(default='', max_length=250)),
                ('my_nickname', models.CharField(default='', max_length=250)),
                ('my_address', models.CharField(default='', max_length=250)),
                ('my_mobile_number', models.CharField(default='', max_length=250)),
                ('my_email', models.EmailField(default='', max_length=250)),
                ('my_birth_day', models.DateField()),
                ('my_crushes', models.CharField(default='', max_length=250)),
                ('my_happiest_moment', models.CharField(default='', max_length=250)),
                ('my_favourite_dishes', models.CharField(default='', max_length=250)),
                ('my_favourite_sports', models.CharField(default='', max_length=250)),
                ('my_favourite_places', models.CharField(default='', max_length=250)),
                ('my_favourite_actor', models.CharField(default='', max_length=250)),
                ('my_favourite_actress', models.CharField(default='', max_length=250)),
                ('my_favourite_webiste', models.CharField(default='', max_length=250)),
                ('my_favourite_festival', models.CharField(default='', max_length=250)),
                ('my_favourite_song', models.CharField(default='', max_length=250)),
                ('my_ideal', models.CharField(default='', max_length=250)),
                ('opinion_about_you', models.CharField(default='', max_length=250)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
