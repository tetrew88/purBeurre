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


	def testIdentificationFormValidity(self):
		self.assertTrue(form.is_valid())


	def testConnexionFormValidity(self)
		self.assertTrue(form.is_valid())