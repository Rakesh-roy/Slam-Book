from django import forms
from django.contrib.auth.models import User

from Friends.models import SlamBook
from django.contrib.auth.forms import UserCreationForm


class SlamBookForm(forms.ModelForm):
    class Meta:
        model = SlamBook
        fields = '__all__'
            # ['my_name', 'my_nickname', 'my_address',
            #       'my_mobile_number', 'my_email', 'my_birth_day',
            #       'my_crushes', 'my_happiest_moment', 'my_favourite_dishes',
            #       'my_favourite_sports', 'my_favourite_places', 'my_favourite_actor',
            #       'my_favourite_actress', 'my_favourite_webiste', 'my_favourite_festival',
            #       'my_favourite_song', 'my_goal', 'opinion_about_you', 'my_profile']


class RegitrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
