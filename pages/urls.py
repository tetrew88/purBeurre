#!/usr/bin/python3

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^login/$', views.connexion, name='connexion'),
    url(r'^logon/$', views.inscription, name='inscription')
]

app_name = 'pages'