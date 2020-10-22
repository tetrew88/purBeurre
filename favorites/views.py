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
		user = request.POST.get('user')

		print(user)

		if productName != None and substituteName != None and user != None:
			product = searchProductInDatabase(productName)
			substitute = searchProductInDatabase(substituteName)

			favorite = Favorites(product=product, substitute=substitute)

			favorite.save()

			product.favorites.add(favorite)
			print("produit ajouter")

	return render(request, template, locals())