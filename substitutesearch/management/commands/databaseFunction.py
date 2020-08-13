from substitutesearch.models import *

import json
import requests

def addProductInDatabase(productData, categoriesList):
	productCategoriesList = []

	try:
		product = Product(name = productData['product_name'],
			ingredients = productData['ingredients_text'],
			label = productData['brands'],
			saturatedFat = productData['nutrient_levels']['saturated-fat'],
			fat = productData['nutrient_levels']['fat'],
			salt = productData['nutrient_levels']['salt'],
			sugar = productData['nutrient_levels']['sugars'],
			allergen = productData['ingredients_text_with_allergens'],
			nutriscore = productData['nutriments']['nutrition-score-fr'],
			url = productData['url'],
			pictureUrl = productData['image_small_url']
		)
	except KeyError:
		print("produit invalide")
		return False 


	for category in categoriesList:
		url = "https://fr.openfoodfacts.org/cgi/search.pl?categories={}&action=process&page_size=100&json=1".format(category.replace(' ', '+'))

		tmpCategory = searchCategoryInDatabase(category)
		if tmpCategory:
			productCategoriesList.append(tmpCategory[0])
			print("catégorie deja existante")
		else:
			productCategory = Category(name=category, url=url)

			productCategory.save()
			productCategoriesList.append(productCategory)
			print("catégorie enregistrer")


	tmpProduct = searchProductInDatabase(productData['product_name'])
	if tmpProduct:
		print("produit deja existant")
	else:
		product.save()

		for element in productCategoriesList:
			product.category.add(element)

		print("produit ajouter")


	return True


def searchProductInDatabase(name):
	product = Product.objects.filter(name__icontains = name)

	if len(product) > 0:
		return product
	else:
		return False


def searchCategoryInDatabase(name):
	category = Category.objects.filter(name__icontains = name)

	if len(category) == 0:
		return False
	else:
		return category


def searchProductOnOFF(keyword):
	url = 'https://fr.openfoodfacts.org/cgi/search.pl?search_terms={}&search_simple=1&action=process&json=1'.format(keyword)

	try:
		result = requests.get(url)
		result = json.loads(result.text)['products'][0]
	except:
		result = False

	return result


def searchSubstitute(categoryName, nuitriscore):
	pass()