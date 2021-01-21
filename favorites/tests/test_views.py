from django.test import TestCase, Client
from django.contrib.auth.models import User

from authentification.models import Profil


# Create your tests here.
class TestFavorite(TestCase):
	""" class testing the authentfication """

	fixtures = ['fixture.json']

	client = Client()

	def test_AddFavorite(self):
		""" test adding a favorite of an user """
		self.user = User.objects.create(username='test',
			first_name='test',
			last_name='test',
			email='test@test.fr')

		self.user.set_password("test")
		self.user.save()

		profil = Profil(name='test', mailAdress='test', user=self.user)

		profil.save()

		self.client.login(username='test', password='test')

		response = self.client.post('/favorites/addToFavorites/', {'substituteName': 'Curly', 'productName': 'nutella'})

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/resultSearch.html')

	def test_ShowFavorite(self):
		pass