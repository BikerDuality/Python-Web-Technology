"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('mainsite/', include('mainsite.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path

from . import views

app_name='mainsite'
urlpatterns = [
    path('',views.home_page,name='homepage'),
    path('<post_name>/',views.show_post,name='post'),
    path('<post_name>/like/',views.post_like_post,name='post_like_post'),
    path('<post_name>/dislike/',views.post_dislike_post,name='post_dislike_post'),
]