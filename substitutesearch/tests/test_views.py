from django.test import TestCase, Client

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


class TestSubstituteSearch(TestCase):
	""" class testing the authentfication """

	fixtures = ['fixture.json']

	client = Client()

	def test_Search(self):
		""" test search of a product """

		response = self.client.post('/searchSubstitute/search/', {'keyword': 'curly'})

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/resultSearch.html')

	def test_Detail(self):
		response = self.client.post('/searchSubstitute/detail/', {'keyword': 'curly'})

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/detail.html')


class TestSeleniumSubstituteSearch(StaticLiveServerTestCase):

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

	def test_search(self):
		self.selenium.get('%s%s' % (self.live_server_url, '/'))
		keyword_input = self.selenium.find_element_by_name("keyword")
		keyword_input.send_keys('poulet')
		keyword_input.send_keys(Keys.RETURN)

		self.selenium.find_element_by_xpath("//div[contains(@class,'resultBanner')]")


	def test_detail(self):
		self.selenium.get('%s%s' % (self.live_server_url, '/'))
		keyword_input = self.selenium.find_element_by_name("keyword")
		keyword_input.send_keys('poulet')
		keyword_input.send_keys(Keys.RETURN)

		skeyword_input = self.selenium.find_element_by_name("detail").click()

		self.selenium.find_element_by_xpath("//div[contains(@class,'productPresentation')]")