from django.test import TestCase, Client

# Create your tests here.
class TestAuthentification(TestCase):
	""" class testing the authentfication """

	client = Client()

	def test_Inscription(self):
		""" test inscription of an user """
		
		response = self.client.post('/authentification/register/', {'name': 'test', 'mailAdress': 'test@test.fr', 'password': '123456'})
		
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/register.html')

	def test_Connexion(self):
		response = self.client.post('/authentification/login/', {'name': 'test', 'password': '123456'})

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/index.html')