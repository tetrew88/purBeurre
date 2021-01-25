import unittest

from substitutesearch.models import Product, Category


class TestSubstituteSearch(unittest.TestCase):
	""" class testing substitutesearch models """

	def test_category(self):
		""" test category model"""
		self.category = Category(name='apéritif', url='http://apéritif.fr')

		self.assertEquals(self.category.name, 'apéritif')


	def test_product(self):
		""" test product model """
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
		
		self.assertEquals(self.product.name, 'curly')