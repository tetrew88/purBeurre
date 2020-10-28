from django.shortcuts import render

from .forms import *
from .models import *

from substitutesearch.models import *
from substitutesearch.management.commands.databaseFunction import *

# Create your views here.
def addToFavorite(request):
	favoritesForm = FavoriteForm()

	template = 'pages/index.html'

	if request.method == 'POST':
		favoritesForm = FavoriteForm(request.POST)


		productName = request.POST.get('productName')
		substituteName = request.POST.get('substituteName')
		user = request.user

		if productName != None and substituteName != None and user != None:
			product = searchProductInDatabase(productName)
			substitute = searchProductInDatabase(substituteName)
			user = searchProfil(user.username)

			favorite = Favorites(product=product[0], substitute=substitute[0])

			favorite.save()

			user[0].favorites.add(favorite)
			print("produit ajouter")

	return render(request, template, locals())


def showFavorites(request):
	template = 'pages/favorites.html'
	
	productCounteur = 0

	favorites = {}
	productList = favoritesList = []

	if request.method == 'GET':
		user = request.user
		user = searchProfil(user.username)

		user = user[0]

		favoritesList = user.favorites.all()

		for favorite in favoritesList:
			if favorite.product.name not in productList:
				productList.append(favorite.product)

		for product in productList:
			favorites[product.name] = []

		for favorite in favoritesList:
			favorites[favorite.product.name].append(favorite.substitute)

		productCounteur = len(productList)

		print("\n\n" + str(favorites) + "\n\n")

	return render(request, template, locals())