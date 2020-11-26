#!/usr/bin/python3

from django.conf.urls import url

from . import views


urlpatterns = [
	 url(r'^index/$', views.index, name='index'),
	 url(r'^legalMention/$', views.legalMention, name='legalMention')
]

app_name = 'pages'