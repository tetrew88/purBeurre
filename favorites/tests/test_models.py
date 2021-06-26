import unittest

from substitutesearch.models import Product
from favorites.models import Favorites


class TestFavorite(unittest.TestCase):
	""" classes testing favoite models """
	
	def test_favorite(self):
		self.product = Product(name='curly',
			ingredients='cacahuete, sel',
			label='curly',
			saturatedFat='low',
			fat='low',
			salt='hight',
			sugar='low',
			allergen='arachide',
			nutriscore='b',
			url='test_url',
			pictureUrl='test_picture_url')

		self.substitute = Product(name='3D',
			ingredients='cacahuete, sel',
			label='3D',
			saturatedFat='low',
			fat='low',
			salt='hight',
			sugar='low',
			allergen='arachide',
			nutriscore='A',
			url='test_url',
			pictureUrl='test_picture_url')

		self.favorite = Favorites(substitute=self.substitute, product=self.product)
		
		self.assertEquals(self.favorite.substitute.name, self.substitute.name)
		self.assertEquals(self.favorite.product.name, self.product.name)