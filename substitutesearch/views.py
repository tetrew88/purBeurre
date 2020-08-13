from django.shortcuts import render

import requests
import json

from .forms import *
from .models import *

from .management.commands.databaseFunction import *

def search(request):
	result = False
	product = False

	productCategoriesList = []
	searchForm = SearchForm()

	tmpCategory = ""

	template = 'pages/index.html'

	if request.method == 'POST':
		identifiantForm = SearchForm(request.POST)

		if identifiantForm.is_valid():
			keyword = request.POST.get('keyword')

			databaseProduct = searchProductInDatabase(keyword)


			if databaseProduct == False:
				result = searchProductOnOFF(keyword)

				if result: 
					categoriesList = result['categories'].split(',')
					for category in categoriesList:
						if category[0] == " ":
							productCategoriesList.append(category[1:])

					addProductInDatabase(result, productCategoriesList)

					product = result

			
			else:
				product = databaseProduct

		if product:
			print("produit trouver")

		else:
			print("produit rechercher non trouver")

	return render(request, template, locals())