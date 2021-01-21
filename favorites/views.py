from django.shortcuts import render

from .models import Favorites

from substitutesearch.views import search

from substitutesearch.forms import SearchForm, DetailForm

from substitutesearch.management.commands.databaseFunction import searchProductInDatabase, searchProfil


def addToFavorite(request):

	if request.method == 'POST':
		"""collect information from the form"""

		productName = request.POST.get('productName')
		substituteName = request.POST.get('substituteName')
		user = request.user

		if substituteName is not None and user is not None:
			"""collect product/substitute information from database"""

			substitute = searchProductInDatabase(substituteName)
			product = searchProductInDatabase(productName)

			"""search user profil"""
			profil = searchProfil(user.username)

			"""create favorite"""
			favorite = Favorites(substitute=substitute[0], product=product[0])
			favorite.save()

			"""add favorite to user profil"""
			profil[0].favorites.add(favorite)

		request.POST._mutable = True
		request.POST['keyword'] = productName
		request.POST._mutable = False

	"""return to the search"""
	return search(request)


def showFavorites(request):
	template = 'pages/favorites.html'

	favoritesList = []

	if request.method == 'GET':
		"""collecte the user profil"""
		user = request.user
		profil = searchProfil(user.username)

		profil = profil[0]

		"""collect user favorite in list"""
		favoritesList = profil.favorites.all()

	return render(request, template, {'detailForm': DetailForm(),
		'searchForm': SearchForm(),
		'favoritesList': favoritesList})