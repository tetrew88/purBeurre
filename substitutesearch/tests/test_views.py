from django.test import TestCase, Client

class TestSubstituteSearch(TestCase):
	""" class testing the authentfication """

	client = Client()

	def test_Search(self):
		""" test search of a product """
		
		response = self.client.post('/searchSubstitute/search/', {'keyword': 'curly'})

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/resultSearch.html')

	def test_Detail(self):
		response = self.client.post('/searchSubstitute/detail/', {'keyword': 'curly'})

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/resultSearch.html')