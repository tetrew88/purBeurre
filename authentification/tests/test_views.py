from django.test import TestCase, Client

# Create your tests here.
class TestAuthentification(TestCase):
	""" class testing the authentfication """

	self.client = Client()

	def testInscription(self)
		""" test inscription of an user """
		
		response = self.client.post('/register/', {'name': 'test', 'mailAdress': 'test@test.fr', 'password': '123456'})
		
		self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, '/')


    def testConnexion(self):
    	response = self.client.post('/register/', {'name': 'test', 'password': '123456'})
		
		self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, '/')