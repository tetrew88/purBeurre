#!/usr/bin/python3

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^login/$', views.connexion, name='connexion'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.deconnexion, name='deconnexion')
]

app_name = 'authentification'