from django.test import TestCase, Client
from django.contrib.auth.models import User

from authentification.models import Profil


class TestAuthentification(TestCase):
	""" class testing the authentfication """

	client = Client()

	def test_index(self):

		response = self.client.post('/')

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/index.html')

	def test_account(self):
		self.user = User.objects.create(username='testouille',
			first_name='testouille',
			last_name='test',
			email='testouille@testouille.fr')

		self.user.set_password("test")
		self.user.save()

		profil = Profil(name=self.user.username, mailAdress=self.user.email, user=self.user)

		profil.save()

		self.client.login(username='testouille', password='test')

		response = self.client.post('/account')

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/account.html')


	def test_legalmention(self):

		response = self.client.post('/legalMention')

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/legalMention.html')