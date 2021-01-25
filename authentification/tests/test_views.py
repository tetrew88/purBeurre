from django.test import TestCase, Client
from django.contrib.auth.models import User

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

# Create your tests here.
class TestAuthentification(TestCase):
	""" class testing the authentfication """

	fixtures = ['fixture.json']

	client = Client()

	def test_inscription(self):
		""" test inscription of an user """

		response = self.client.post('/authentification/register/', {'name': 'test', 'mailAdress': 'test@test.fr', 'password': 'test'})

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/register.html')

	def test_succes_connexion(self):
		response = self.client.post('/authentification/login/', {'mail': 'test@test.fr', 'password': 'test'})
		response = self.client.get('/account')

		self.assertEquals(response.status_code, 200)


	def test_fail_connexion(self):
		response = self.client.post('/authentification/login/', {'mail': 'test', 'password': '123'})
		response = self.client.get('/account')

		self.assertEquals(response.status_code, 401)


class TestSeleniumAuthentification(StaticLiveServerTestCase):
	""" class testing user interaction """

	fixtures = ['fixture.json']

	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		cls.selenium = WebDriver()
		cls.selenium.implicitly_wait(10)

	@classmethod
	def tearDownClass(cls):
		cls.selenium.quit()
		super().tearDownClass()

	def test_login(self):
		""" test login parcours """
		self.selenium.get('%s%s' % (self.live_server_url, '/'))
		self.selenium.find_element_by_xpath("//button[contains(@class,'fa fa-user fa-2x')]").click()

		username_input = self.selenium.find_element_by_name("mail")
		username_input.send_keys('test@test.fr')
		password_input = self.selenium.find_element_by_name("password")
		password_input.send_keys('test')

		self.selenium.find_element_by_id('connexionButton').click()

	def test_invalid_login(self):
		""" test an invalid login parcours """
		self.selenium.get('%s%s' % (self.live_server_url, '/'))
		self.selenium.find_element_by_xpath("//button[contains(@class,'fa fa-user fa-2x')]").click()

		username_input = self.selenium.find_element_by_name("mail")
		username_input.send_keys('test@test.fr')
		password_input = self.selenium.find_element_by_name("password")
		password_input.send_keys('testlouper')

		self.selenium.find_element_by_id('connexionButton').click()

		""" check if error message appaired """
		self.selenium.find_element_by_id('message')


	def test_register(self):
		""" test registering parcours """

		self.selenium.get('%s%s' % (self.live_server_url, '/authentification/register/'))

		username_input = self.selenium.find_element_by_name("name")
		username_input.send_keys('SeleTest')
		mail_input = self.selenium.find_element_by_name("mail")
		mail_input.send_keys('SeleTest@selenium.com')
		password_input = self.selenium.find_element_by_name("password")
		password_input.send_keys('test')

		self.selenium.find_element_by_id('inscriptionButton').click()

		self.selenium.find_element_by_id('contact')


	def test_registration_error(self):
		""" test an invalid registering parcours """
		self.selenium.get('%s%s' % (self.live_server_url, '/authentification/register/'))

		username_input = self.selenium.find_element_by_name("name")
		username_input.send_keys('test')
		mail_input = self.selenium.find_element_by_name("mail")
		mail_input.send_keys('SeleTest@selenium.com')
		password_input = self.selenium.find_element_by_name("password")
		password_input.send_keys('test')

		self.selenium.find_element_by_id('inscriptionButton').click()

		""" check if error message appaired """
		self.selenium.find_element_by_id('message')
