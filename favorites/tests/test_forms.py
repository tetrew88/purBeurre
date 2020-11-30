from django.test import TransactionTestCase

from .forms import *


class TestFavoriteForm(TransactionTestCase):
	""" classe testing authentification form """

	FavoriteForm = RegisterForm(data={
		'productName': 'nutella',
		'substituteName': 'pate a tartiné'
		})


	def test_FavoriteFormValidity(self):
		self.assertTrue(FavoriteForm.is_valid())