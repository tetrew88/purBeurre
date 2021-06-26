#!/usr/bin/python3

from django.conf.urls import url

from . import views


urlpatterns = [
	 url(r'^search/$', views.search, name='search'),
	 url(r'^detail/$', views.detail, name='detail')
]

app_name = 'substitutesearch'