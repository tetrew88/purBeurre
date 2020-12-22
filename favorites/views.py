from django.shortcuts import render

from .forms import *
from .models import *

from substitutesearch.views import *

from authentification.forms import *
from substitutesearch.forms import *

from substitutesearch.models import *
from substitutesearch.management.commands.databaseFunction import *

# Create your views here.
def addToFavorite(request):
	searchForm = SearchForm()
	identifiantForm = IdentificationForm()
	favoriteForm = FavoriteForm()

	if request.method == 'POST':
		favoritesForm = FavoriteForm(request.POST)

		productName = request.POST.get('productName')
		substituteName = request.POST.get('substituteName')
		user = request.user

		if substituteName != None and user != None:
			substitute = searchProductInDatabase(substituteName)
			profil = searchProfil(user.username)

			favorite = Favorites(substitute=substitute[0])

			favorite.save()

			profil[0].favorites.add(favorite)
			print("produit ajouter")

		request.POST._mutable = True
		request.POST['keyword'] = productName
		request.POST._mutable = False

	return search(request)


def showFavorites(request):
	detailForm = DetailForm()
	searchForm = SearchForm()
	identifiantForm = IdentificationForm()
	favoriteForm = FavoriteForm()
	
	template = 'pages/favorites.html'
	
	productCounteur = 0

	favorites = {}
	productList = favoritesList = []

	if request.method == 'GET':
		user = request.user
		profil = searchProfil(user.username)

		profil = profil[0]

		favoritesList = profil.favorites.all()
		productCounteur = len(productList)

		"""
			for favorite in favoritesList:
				if favorite.product.name not in productList:
					productList.append(favorite.product)

			for product in productList:
				favorites[product.name] = []

			for favorite in favoritesList:
				favorites[favorite.product.name].append(favorite.substitute)

			print("\n\n" + str(favorites) + "\n\n")
		"""

	return render(request, template, locals())