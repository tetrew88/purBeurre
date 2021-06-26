from django.test import TestCase, Client
from django.contrib.auth.models import User

from authentification.models import Profil


# Create your tests here.
class TestFavorite(TestCase):
	""" class testing the authentfication """

	fixtures = ['fixture.json']

	client = Client()

	def test_add_Favorite(self):
		""" test adding a favorite of an user """
		self.user = User.objects.create(username='testouille',
			first_name='testouille',
			last_name='test',
			email='testouille@testouille.fr')

		self.user.set_password("test")
		self.user.save()

		profil = Profil(name=self.user.username, mailAdress=self.user.email, user=self.user)

		profil.save()

		self.client.login(username='testouille', password='test')

		response = self.client.post('/favorites/addToFavorites/', {'substituteName': 'Curly', 'productName': 'nutella'})

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/resultSearch.html')

	def test_show_favorite(self):
		"""test showing favorites"""

		self.user = User.objects.create(username='testouille',
			first_name='testouille',
			last_name='test',
			email='testouille@testouille.fr')

		self.user.set_password("test")
		self.user.save()

		profil = Profil(name=self.user.username, mailAdress=self.user.email, user=self.user)

		profil.save()

		self.client.login(username='testouille', password='test')

		response = self.client.post('/favorites/showFavorites/', {})

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/favorites.html')