from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

import requests
import json

from pages.forms import *
from .models import *

from .management.commands.databaseFunction import *

from favorites.forms import *
from authentification.forms import *
from .forms import *


def search(request):
	result = False
	product = False

	productCategoriesList = substituteList = []
	
	searchForm = SearchForm()
	detailForm = DetailForm()
	identifiantForm = IdentificationForm()
	favoriteForm = FavoriteForm()

	tmpCategory = ""

	template = 'pages/resultSearch.html'

	if request.method == 'POST':
		searchForm = SearchForm(request.POST)

		if searchForm.is_valid():
			keyword = request.POST.get('keyword')

			#cherche le produit dans la base de donnée
			product = searchProductInDatabase(keyword)

			#si le produit n'as pas ete trouver le cherche sur off
			if product == False:
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

		#si un produit est valide
		if product:
			print("produit trouver")

			product = product[0]

			#cherche les substituts du produits
			substituteList = searchSubstitute(product)

			request.method = 'GET'
			request.GET._mutable = True 
			request.GET['substituteList'] = substituteList
			request.GET._mutable = False

			return listing(request)
		
		else:
			print("produit rechercher non trouver")

	if request.method == 'GET':
		print('getttt')

	return render(request, template, locals())


def listing(request):
	template = 'pages/resultSearch.html'
	paginate = True

	if request.method == 'GET':

		page = request.GET.get('page')
		substituteList = request.GET.get('substituteList')

		print(request.GET)

		paginator = Paginator(substituteList, 9)

		try:
			substitutes = paginator.page(page)
		except PageNotAnInteger:
			substitutes = paginator.page(1)
		except EmptyPage:
			substitutes = paginator.page(paginator.num_pages)

	return render(request, template, locals())


def detail(request):
	searchForm = SearchForm()
	detailForm = DetailForm()

	identifiantForm = IdentificationForm()
	favoriteForm = FavoriteForm()

	template = 'pages/detail.html'

	if request.method == 'POST':
		print(request.POST)
		detailForm = DetailForm(request.POST)

		if detailForm.is_valid():
			keyword = request.POST.get('keyword')

			#cherche le produit dans la base de donnée
			product = searchProductInDatabase(keyword)

			product = product[0]

	return render(request, template, locals())