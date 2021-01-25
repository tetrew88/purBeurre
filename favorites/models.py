from django.db import models

from substitutesearch.models import Product


class Favorites(models.Model):
	""" Favorites was composed of one product and one substitute """
	substitute = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='substitute', default=None)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product', default=None)