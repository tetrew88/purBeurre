from django.conf.urls import url

from . import views


urlpatterns = [
	 url(r'^(?P<productId>)/$', views.addToFavorite, name='addToFavorites'),
]
app_name = 'favorites'