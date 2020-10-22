from django.db import models

from django.contrib.auth.models import User
from substitutesearch.models import *

class Favorites(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'product', default=None)
	substitute = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'substitute', default=None)