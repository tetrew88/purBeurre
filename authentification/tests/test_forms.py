from django.test import TransactionTestCase

from authentification.forms import RegisterForm, IdentificationForm


class TestAuthentificationForm(TransactionTestCase):
	""" classe testing authentification form """

	def test_register_form_validity(self):
		registerForm = RegisterForm(data={
		'name': 'test',
		'mail': 'test@test.fr',
		'password': '123456'
		})

		self.assertTrue(registerForm.is_valid())

	def test_connexion_form_validity(self):
		connexionForm = IdentificationForm(data={
		'mail': 'test@test.fr',
		'password': '123456'
		})
		self.assertTrue(connexionForm.is_valid())