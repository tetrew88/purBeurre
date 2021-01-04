from django.test import TransactionTestCase

from authentification.forms import *

class TestAuthentificationForm(TransactionTestCase):
	""" classe testing authentification form """

	def test_RegisterFormValidity(self):
		registerForm = RegisterForm(data={
		'name': 'test',
		'mail': 'test@test.fr',
		'password': '123456'
		})

		self.assertTrue(registerForm.is_valid())


	def test_ConnexionFormValidity(self):
		connexionForm = IdentificationForm(data={
		'name': 'test',
		'password': '123456'
		})
		self.assertTrue(connexionForm.is_valid())