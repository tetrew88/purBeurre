from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import requests
import json

from pages.models import *

from .databaseFunction import *

class Command(BaseCommand):

	def initDB(self):
		productCategoriesList = []
		categoriesList = ['Snacks', 'Boissons', 'Viandes', 'Desserts', 'Riz']
		result = []

		url = ""


		#main loop
		for category in categoriesList:
			tmpCategory = False

			url = "https://fr.openfoodfacts.org/cgi/search.pl?categories={}&action=process&page_size=100&json=1".format(category)

			try:
				result = requests.get(url)
				result = json.loads(result.text)
				result = result['products']
			except:
				print("Catégorie introuvable")
				continue

			if result == 0:
				print("aucun produit trouver dans cette catégorie")
			else:
				for product in result:
					try:
						productCategoriesList = product['categories'].split(',')
					except KeyError:
						print("produit invalide")
						continue
					
					for category in productCategoriesList:
						if category[0:1] == " ":
							category = category[1:]

					addProductInDatabase(product, productCategoriesList)


		print("collect finised")


	def handle(self, *args, **options):
		self.initDB()