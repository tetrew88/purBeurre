from django.db import models

from django.contrib.auth.models import User

from substitutesearch.models import *


# Create your models here.
class Profil(models.Model):
	name = models.CharField(max_length=100, null = False, unique=True)
	mailAdress = models.EmailField(max_length=100, null = False, unique=True)
	password = models.CharField(max_length=100, null = False)
	user = models.OneToOneField(User, on_delete = models.CASCADE)

	favorites = models.ManyToManyField(Product, related_name = 'product')
