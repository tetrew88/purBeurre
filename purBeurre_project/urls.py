#!/usr/bin/python3

"""purBeurre_project URL Configuration

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
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls import url

from pages import views

urlpatterns = [
	url(r'^$', views.index),
    url(r'^authentification/', include('authentification.urls', namespace='authentification')),
	url(r'^account', views.account),
   	url(r'^admin/', admin.site.urls),
    url(r'^searchSubstitute/', include('substitutesearch.urls', namespace='search')),
    url(r'^favorites/', include('favorites.urls', namespace='favorites')),
    url(r'^legalMention', views.legalMention),
]
