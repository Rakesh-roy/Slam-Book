"""Friends_Album URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Friends import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('login/', views.login_user, name='login_user'),
    path('create_user/', views.create_user, name='create_user'),
    path('logout/', views.logout_user, name='logout_user'),

    path('slam_home/', views.slam_home, name='slam_home'),
    path('slam_home/make_slam/', views.make_slam, name='make_slam'),
    path('slam_home/view_slam/', views.view_slam, name='view_slam'),
    path('slam_home/view_slam/view_friend/', views.view_friend, name='view_friend'),
    path('slam_home/view_slam/remove_friend/', views.remove_friend, name='remove_friend'),
    path('slam_home/view_slam/edit_friend/', views.edit_friend, name='edit_friend'),

    path('slam_home/search_friend/', views.search_friend, name='search_friend'),

    path('about_us/', views.about_us, name='about_us'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
