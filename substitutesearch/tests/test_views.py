from django.test import TestCase

class TestSubstituteSearch(TestCase):
	""" class testing the authentfication """

	self.client = Client()

	def test_Search(self)
		""" test inscription of an user """
		
		response = self.client.post('/search/', {'keyword': 'nutella'})
		
		self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/resultSearch.html')


    def test_Detail(self):
    	response = self.client.post('/searchSubstitute/detail/', {'keyword': 'nutella'})
		
		self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/resultSearch.html')