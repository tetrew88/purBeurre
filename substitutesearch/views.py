from django.shortcuts import render

from .management.commands.databaseFunction import searchProductInDatabase, searchProductOnOFF, addProductInDatabase, searchSubstitute

from favorites.forms import FavoriteForm
from authentification.forms import IdentificationForm
from .forms import SearchForm, DetailForm


def search(request):
	result = False
	product = False

	productCategoriesList = substituteList = []

	template = 'pages/resultSearch.html'

	if request.method == 'POST':
		searchForm = SearchForm(request.POST)

		if searchForm.is_valid():
			keyword = request.POST.get('keyword')

			"""cherche le produit dans la base de donnée"""
			product = searchProductInDatabase(keyword)

			"""si le produit n'as pas ete trouver le cherche sur off"""
			if product is False:
				result = searchProductOnOFF(keyword)

				if result:
					categoriesList = result['categories'].split(',')
					for category in categoriesList:
						if category[0] == " ":
							productCategoriesList.append(category[1:])
						else:
							productCategoriesList.append(category)

					if addProductInDatabase(result, productCategoriesList):
						product = searchProductInDatabase(keyword)
					else:
						pass

		"""si un produit est valide"""
		if product:
			print("produit trouver")

			product = product[0]

			"""cherche les substituts du produits"""
			substituteList = searchSubstitute(product)

	return render(request, template, {'detailForm': DetailForm(),
		'searchForm': SearchForm(), 'identifiantForm': IdentificationForm(), 'favoriteForm': FavoriteForm(),
		'product': product, 'substituteList': substituteList})


def detail(request):
	detailForm = DetailForm()

	template = 'pages/detail.html'

	if request.method == 'POST':
		print(request.POST)
		detailForm = DetailForm(request.POST)

		if detailForm.is_valid():
			keyword = request.POST.get('keyword')

			"""cherche le produit dans la base de donnée"""
			product = searchProductInDatabase(keyword)

			product = product[0]

	return render(request, template, {'detailForm': DetailForm(),
		'searchForm': SearchForm(), 'identifiantForm': IdentificationForm(),
		'product': product})