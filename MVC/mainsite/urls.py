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
from django.urls import path

from . import views

app_name='mainsite'
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('about/',views.about,name='about'),
    path('list/',views.show_list,name='list'),
    path('list/order=<order>/',views.show_list,name='order_list'),
    path('list/filter=<filter>/',views.show_list,name='filter_list'),
    path('list/<sku>/',views.detail,name='detail'),
]
