from django.shortcuts import render

from .models import Favorites

from substitutesearch.views import search

from substitutesearch.forms import SearchForm, DetailForm

from substitutesearch.management.commands.database_function import search_product_in_database, search_profil


def addToFavorite(request):
	""" 
		view used for adding a substitute/product to favorites:
			1) collect product name and substitute name from favorite Form.
				collect user from the request
			2)collect substitute and product informations to database
			3)search the profil of the user
			4)add favorite to user
			5)adapting the post request for search view
			5)redirect user to the search views
	"""

	if request.method == 'POST':
		"""collect information from the form"""

		productName = request.POST.get('productName')
		substituteName = request.POST.get('substituteName')
		user = request.user

		if substituteName is not None and user is not None:
			"""collect product/substitute information from database"""

			substitute = search_product_in_database(substituteName)
			product = search_product_in_database(productName)

			"""search user profil"""
			profil = search_profil(user.username)

			"""create favorite"""
			favorite = Favorites(substitute=substitute[0], product=product[0])
			favorite.save()

			"""add favorite to user profil"""
			profil[0].favorites.add(favorite)

		""" adapt the post request for search view """
		request.POST._mutable = True
		request.POST['keyword'] = productName
		request.POST._mutable = False

	"""return to the search"""
	return search(request)


def showFavorites(request):
	"""
		function for display the user favorites

		1)collect user from the post request
		2)search the associated profil
		3)collect favorites from profil
	"""
	template = 'pages/favorites.html'

	favoritesList = []

	if request.method == 'GET':
		"""collecte the user profil"""
		user = request.user
		profil = search_profil(user.username)

		profil = profil[0]

		"""collect user favorite in a list"""
		favoritesList = profil.favorites.all()

	return render(request, template, {'detailForm': DetailForm(),
		'searchForm': SearchForm(),
		'favoritesList': favoritesList})