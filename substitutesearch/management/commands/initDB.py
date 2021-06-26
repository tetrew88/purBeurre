import requests
import json

from django.core.management.base import BaseCommand

from .database_function import add_product_in_database


class Command(BaseCommand):

	def initDB(self):
		""" 
			Méthode for initialised database:
				1)collect 100 product by category to openfoodfact
				2)collect each categories of each product
				3)add product in database
		"""

		productCategoriesList = []
		categoriesList = ['Snacks', 'Boissons', 'Viandes', 'Desserts', 'Riz']
		result = []

		url = ""

		"""main loop"""
		for category in categoriesList:
			""" collect 100 product by category """
			url = "https://fr.openfoodfacts.org/cgi/search.pl?categories={}&action=process&page_size=100&json=1".format(category)

			try:
				result = requests.get(url).json()
				result = result['products']
			except:
				print("Catégorie introuvable")
				continue

			if result == 0:
				print("aucun produit trouver dans cette catégorie")
			else:
				""" collect each categories of each product """
				for product in result:
					try:
						productCategoriesList = product['categories'].split(',')
					except KeyError:
						print("produit invalide")
						continue

					for category in productCategoriesList:
						if category[0:1] == " ":
							category = category[1:]

					""" add product in database """
					add_product_in_database(product, productCategoriesList)

		print("collect finised")

	def handle(self, *args, **options):
		self.initDB()