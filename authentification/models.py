from django.db import models

from django.contrib.auth.models import User

from favorites.models import Favorites


# Create your models here.
class Profil(models.Model):
	"""
		user profil composed by:
			username
			mail adress
			user linking to the profil

			favorites of the user
	"""
	
	name = models.CharField(max_length=100, null=False, unique=True)
	mailAdress = models.EmailField(max_length=100, null=False, unique=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	favorites = models.ManyToManyField(Favorites, related_name='favorites')