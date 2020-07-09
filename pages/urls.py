#!/usr/bin/python3

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^login/$', views.connexion, name='connexion'),
]

app_name = 'pages'