from django.contrib.auth.models import User
from django.db import models


class SlamBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slam_no = models.AutoField(primary_key=True)
    my_name = models.CharField(max_length=250,default='')
    my_nickname = models.CharField(max_length=250,default='')
    my_address = models.CharField(max_length=250,default='')
    my_mobile_number = models.CharField(max_length=250,default='')
    my_email = models.EmailField(max_length=250,default='')
    my_birth_day = models.DateField()
    my_crushes = models.CharField(max_length=250,default='')
    my_happiest_moment = models.CharField(max_length=250,default='')
    my_favourite_dishes = models.CharField(max_length=250,default='')
    my_favourite_sports = models.CharField(max_length=250,default='')
    my_favourite_places = models.CharField(max_length=250,default='')
    my_favourite_actor = models.CharField(max_length=250,default='')
    my_favourite_actress = models.CharField(max_length=250,default='')
    my_favourite_song = models.CharField(max_length=250,default='')
    my_goal = models.CharField(max_length=250,default='')
    opinion_about_you = models.CharField(max_length=250,default='')
    created_date = models.DateTimeField(auto_now=True)
    my_profile = models.ImageField(upload_to='slam_images/', blank=True, null=True)

    def __str__(self):
        return self.my_name
