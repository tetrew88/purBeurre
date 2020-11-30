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


	def test_SearchFormValidity(self):
		self.assertTrue(searchForm.is_valid())


	def test_DetailFormValidity(self)
		self.assertTrue(searchForm.is_valid())