from django.test import TestCase, Client
from django.contrib.auth.models import User


# Create your tests here.
class TestAuthentification(TestCase):
	""" class testing the authentfication """

	client = Client()

	def test_Inscription(self):
		""" test inscription of an user """

		response = self.client.post('/authentification/register/', {'name': 'test', 'mailAdress': 'test@test.fr', 'password': '123456'})

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/register.html')

	def test_SuccesConnexion(self):
		self.user = User.objects.create(username='test',
			first_name='test',
			last_name='test',
			email='test@test.fr')

		self.user.set_password("test")
		self.user.save()

		response = self.client.post('/authentification/login/', {'mail': 'test@test.fr', 'password': 'test'})

		self.assertEquals(response.status_code, 302)

	def test_FailConnexion(self):
		self.user = User.objects.create(username='test',
			first_name='test',
			last_name='test',
			email='test@test.fr')

		self.user.set_password("test")
		self.user.save()

		response = self.client.post('/authentification/login/', {'mail': 'test', 'password': '123'})
		response = self.client.get('/account')

		self.assertEquals(response.status_code, 401)