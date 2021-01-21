from django.test import TransactionTestCase

from favorites.forms import FavoriteForm


class TestFavoriteForm(TransactionTestCase):
	""" classe testing authentification form """

	def test_FavoriteFormValidity(self):
		favoriteForm = FavoriteForm(data={
			'productName': 'nutella',
			'substituteName': 'pate a tartiné'
		})

		self.assertTrue(favoriteForm.is_valid())