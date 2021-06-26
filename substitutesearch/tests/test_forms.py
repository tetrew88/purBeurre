from django.test import TransactionTestCase

from substitutesearch.forms import SearchForm, DetailForm


class TestSubstituteSearchForm(TransactionTestCase):
	""" classe testing authentification form """

	def test_SearchFormValidity(self):
		searchForm = SearchForm(data={
		'keyword': 'test'
		})

		self.assertTrue(searchForm.is_valid())

	def test_DetailFormValidity(self):
		detailForm = DetailForm(data={
		'keyword': 'test'
		})

		self.assertTrue(detailForm.is_valid())