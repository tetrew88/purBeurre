from django.db import models

from django.contrib.auth.models import User
from substitutesearch.models import *

class Favorites(models.Model):
	substitute = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'substitute', default=None)