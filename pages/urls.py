#!/usr/bin/python3

from django.conf.urls import url

from . import views


urlpatterns = [
	 url(r'^index/$', views.index, name='index'),
]

app_name = 'pages'