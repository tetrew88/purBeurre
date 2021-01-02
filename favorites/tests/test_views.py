from django.test import TestCase, Client

# Create your tests here.
class TestFavorite(TestCase):
	""" class testing the authentfication """

	self.client = Client()

	def test_AddFavorite(self)
		""" test adding a favorite of an user """
		
		self.client.login(username='test', password='secret')

		response = self.client.post('/favorites/addToFavorites/', {'substituteName': 'Curly donuts cacahuètes '})
		
		self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, '/')


    def test_ShowFavorite(self):
    	pass