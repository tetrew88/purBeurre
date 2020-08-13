#!/usr/bin/python3

from django.conf.urls import url

from . import views


urlpatterns = [
	 url(r'^search/$', views.search, name='search'),
]

app_name = 'substitutesearch'