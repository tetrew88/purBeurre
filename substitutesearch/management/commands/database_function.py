from substitutesearch.models import Product, Category
from authentification.models import Profil

import json
import requests


def add_product_in_database(productData, categoriesList):
	"""
		function for add a product to the database:
		1)try to create a product
		2)for each category of the product create a category
			check if the category wasn't already in database
		3) save category
		4)check if the product wasn't already in database
		5)save product
	"""
	productCategoriesList = []

	try:
		""" try to create a product """
		product = Product(name=productData['product_name'],
			ingredients=productData['ingredients_text'],
			label=productData['brands'],
			saturatedFat=productData['nutrient_levels']['saturated-fat'],
			fat=productData['nutrient_levels']['fat'],
			salt=productData['nutrient_levels']['salt'],
			sugar=productData['nutrient_levels']['sugars'],
			allergen=productData['ingredients_text_with_allergens'],
			nutriscore=productData['nutriments']['nutrition-score-fr'],
			url=productData['url'],
			pictureUrl=productData['image_small_url']
		)
	except KeyError:
		return False

	for category in categoriesList:
		""" for each category of the product create a category """
		url = "https://fr.openfoodfacts.org/cgi/search.pl?search_terms={}&search_simple=1&action=process".format(category.replace(' ', '+'))

		""" check if the category wasn't already in database """
		tmpCategory = search_category_in_database(category)
		if tmpCategory:
			productCategoriesList.append(tmpCategory[0])
		else:
			productCategory = Category(name=category, url=url)

			productCategory.save()
			productCategoriesList.append(productCategory)

	""" check if the product wasn't already in database """
	tmpProduct = search_product_in_database(productData['product_name'])
	if tmpProduct:
		print("produit deja existant")
	else:
		product.save()

		for element in productCategoriesList:
			product.category.add(element)

		print("produit ajouter")

	return True


def search_product_in_database(name):
	""" function call for search a product in the database """

	product = Product.objects.all().filter(name__icontains=name)

	if not product.exists():
		return False
	else:
		return product


def search_category_in_database(name):
	""" function call for search a category in the database """
	category = Category.objects.all().filter(name__icontains=name)

	if not category.exists():
		return False
	else:
		return category


def search_product_on_off(keyword):
	""" function call for search a product on openfoodfact """
	url = 'https://fr.openfoodfacts.org/cgi/search.pl?search_terms={}&search_simple=1&action=process&json=1'.format(keyword)

	try:
		result = requests.get(url)
		result = json.loads(result.text)['products'][0]
	except:
		result = False

	return result


def search_substitute(product):
	"""
		function allowing to search substitutes of an product 
			1)collect categories of the product
			2)collect each product of each categories
			3)test if the substitute has a best nutriscore of product
	"""
	categoriesList = substituteList = []

	""" collect categories of the product """
	categoriesList = product.category.all()

	for category in categoriesList:
		""" collect each product of each categories """
		productList = Product.objects.all()

		if productList.exists():
			for element in productList:
				if category in element.category.all():
					if element.name != product.name:
						"""test if the substitute has a best nutriscore of product"""
						if element.nutriscore < product.nutriscore:
							substituteList.append(element)

	if len(substituteList) > 0:
		return substituteList
	else:
		return False


def search_profil(userName):
	""" function for find profil associated to an user """
	
	profil = Profil.objects.all()
	profil = profil.filter(name=userName)

	if len(profil) > 0:
		return profil
	else:
		return False