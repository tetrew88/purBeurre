from django.conf.urls import url

from . import views


urlpatterns = [
	 url(r'^addToFavorites/$', views.addToFavorite, name='addToFavorites'),
	 url(r'^showFavorites/$', views.showFavorites, name='showFavorites'),
]
app_name = 'favorites'