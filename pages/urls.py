#!/usr/bin/python3
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^login/$', views.connexion, name='connexion'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = 'pages'