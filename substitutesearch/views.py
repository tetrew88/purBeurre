from django.shortcuts import render

from .management.commands.database_function import search_product_in_database, search_product_on_off, add_product_in_database, search_substitute

from favorites.forms import FavoriteForm
from authentification.forms import IdentificationForm
from .forms import SearchForm, DetailForm


def search(request):
	""" 
		views for search substitute of an product:
			1)collect keyword from search form
			2)search the product associated to keyword in database
				îf he's wasn't found serched him to openfoodfact an add him to database
			3)search substitute
	"""
	result = False
	product = False

	productCategoriesList = substituteList = []

	template = 'pages/resultSearch.html'

	if request.method == 'POST':
		searchForm = SearchForm(request.POST)

		if searchForm.is_valid():
			"""collect keyword from search form"""
			keyword = request.POST.get('keyword')

			"""cherche le produit dans la base de donnée"""
			product = search_product_in_database(keyword)

			"""si le produit n'as pas ete trouver le cherche sur off"""
			if product is False:
				result = search_product_on_off(keyword)

				if result:
					categoriesList = result['categories'].split(',')
					for category in categoriesList:
						if category[0] == " ":
							productCategoriesList.append(category[1:])
						else:
							productCategoriesList.append(category)

					if add_product_in_database(result, productCategoriesList):
						product = search_product_in_database(keyword)
					else:
						pass

		"""si un produit est valide"""
		if product:
			print("produit trouver")

			product = product[0]

			"""cherche les substituts du produits"""
			substituteList = search_substitute(product)

	return render(request, template, {'detailForm': DetailForm(),
		'searchForm': SearchForm(), 'identifiantForm': IdentificationForm(), 'favoriteForm': FavoriteForm(),
		'product': product, 'substituteList': substituteList})


def detail(request):
	""" view for display information of an product """
	detailForm = DetailForm()

	template = 'pages/detail.html'

	if request.method == 'POST':
		print(request.POST)
		detailForm = DetailForm(request.POST)

		if detailForm.is_valid():
			keyword = request.POST.get('keyword')

			"""cherche le produit dans la base de donnée"""
			product = search_product_in_database(keyword)

			product = product[0]

	return render(request, template, {'detailForm': DetailForm(),
		'searchForm': SearchForm(), 'identifiantForm': IdentificationForm(),
		'product': product})