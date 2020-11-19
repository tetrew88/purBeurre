from django.test import TestCase, Client

# Create your tests here.
class TestFavorite(TestCase):
	""" class testing the authentfication """

	self.client = Client()

	def testAddFavorite(self)
		""" test adding a favorite of an user """
		
		self.client.login(username='test', password='secret')

		response = self.client.post('/favorites/addToFavorites/', {'productName': 'nutella', 'substituteName': 'Curly donuts cacahuètes '})
		
		self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, '/')


    def testShowFavorite(self):
    	pass