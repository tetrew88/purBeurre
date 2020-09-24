from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

import requests
import json

from pages.forms import *
from .models import *

from .management.commands.databaseFunction import *

from authentification.forms import *


def search(request):
	result = False
	product = False

	productCategoriesList = substituteList = []
	
	searchForm = SearchForm()
	identifiantForm = IdentificationForm()

	tmpCategory = ""

	template = 'pages/resultSearch.html'

	if request.method == 'POST':
		identifiantForm = SearchForm(request.POST)

		if identifiantForm.is_valid():
			keyword = request.POST.get('keyword')

			product = searchProductInDatabase(keyword)

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

		if product:
			print("produit trouver")
			baseProduct = product[0]
			
			substituteList = searchSubstitute(product[0])

			if substituteList:
				print("substitut trouver")

				paginate = True

				paginator = Paginator(substituteList, 9)
				page = request.GET.get('page')

				try:
					substitutes = paginator.page(page)
				except PageNotAnInteger:
					substitutes = paginator.page(1)
				except EmptyPage:
					substitutes = paginator.page(paginator.num_pages)
		
		else:
			print("produit rechercher non trouver")

	return render(request, template, locals())