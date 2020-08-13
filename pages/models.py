from django.db import models

from django.contrib.auth.models import User

from substitutesearch.models import *

class Profil(models.Model):
	mailAdress = models.EmailField(max_length=100, null = False, unique=True)
	password = models.CharField(max_length=100, null = False)
	user = models.OneToOneField(User, on_delete = models.CASCADE)

	favorites = models.ManyToManyField(Product, related_name = 'product')
