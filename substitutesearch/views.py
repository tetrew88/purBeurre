from django.shortcuts import render

import requests
import json

from pages.forms import *
from .models import *

from .management.commands.databaseFunction import *

def search(request):
	result = False
	product = False

	productCategoriesList = substituteList = []
	searchForm = SearchForm()

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
			substituteList = searchSubstitute(product[0])

			print(substituteList)

		else:
			print("produit rechercher non trouver")

		produit = substituteList[0]

	return render(request, template, locals())