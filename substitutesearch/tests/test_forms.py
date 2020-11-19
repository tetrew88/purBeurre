from django.test import TransactionTestCase

from .forms import *


class TestSubstituteSearchForm(TransactionTestCase):
	""" classe testing authentification form """

	searchForm = SearchForm(data={
		'keyword': 'test'
		})

	detailForm = IdentificationForm(data={
		'keyword': 'test'
		})


	def testSearchFormValidity(self):
		self.assertTrue(searchForm.is_valid())


	def testDetailFormValidity(self)
		self.assertTrue(searchForm.is_valid())