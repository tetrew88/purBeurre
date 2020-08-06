from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import requests
import json

from pages.models import *

class Command(BaseCommand):

	def initDB(self):
		categories_list = ['Snacks', 'Boissons', 'Viandes', 'Desserts', 'Sauces', 'Riz']
		result = []

		url = ""


		#main loop
		for category in categories_list:
			print("1")

			url = "https://fr.openfoodfacts.org/cgi/search.pl?categories={}&action=process&page_size=100&json=1".format(category)

			productCategory = Category(name=category, url=url)

			productCategory.save()

			print("2")

			#request
			result = requests.get(url)

			print(result)
			result = json.loads(result.text)

			print("3")

			result = result['products']

			for product in result:
				data = Product(name = product['product_name'],
		        	ingredients = product['ingredients_text'],
		        	label = product['brands'],
		        	saturatedFat = product['nutrient_levels']['saturated-fat'],
		        	fat = product['nutrient_levels']['fat'],
		        	salt = product['nutrient_levels']['salt'],
		        	sugar = product['nutrient_levels']['sugars'],
		        	allergen = product['ingredients_text_with_allergens'],
		        	nutriscore = product['nutriments']['nutrition-score-fr'],
		        	url = product['url'],
		        	pictureUrl = product['image_small_url']
		        	)
				data.save()
				data.category.add(productCategory)


		print("collect finised")


	def handle(self, *args, **options):
		self.initDB()