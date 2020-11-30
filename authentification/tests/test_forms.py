from django.test import TransactionTestCase

from .forms import *

class TestAuthentificationForm(TransactionTestCase):
	""" classe testing authentification form """

	registerForm = RegisterForm(data={
		'name': 'test',
		'mail': 'test@test.fr',
		'password': '123456'
		})

	connexionForm = IdentificationForm(data={
		'name': 'test',
		'password': '123456'
		})


	def test_IdentificationFormValidity(self):
		self.assertTrue(registerForm.is_valid())


	def test_ConnexionFormValidity(self)
		self.assertTrue(registerForm.is_valid())