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

		response = self.client.post('/authentification/login/', {'name': 'test', 'password': 'test'})

		self.assertEquals(response.status_code, 302)
		self.assertTemplateUsed(response, 'pages/index.html')


	def test_FailConnexion(self):
		self.user = User.objects.create(username='test',
			first_name='test',
			last_name='test',
			email='test@test.fr')

		self.user.set_password("test")
		self.user.save()

		response = self.client.post('/authentification/login/', {'name': 'test', 'password': '123'})

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/index.html')