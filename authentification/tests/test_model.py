import unittest

from django.contrib.auth.models import User

from authentification.models import Profil


class TestProfil(unittest.TestCase):
	""" test profil model """
	
	def test_profil(self):
		self.user = User.objects.create(username='testouille',
			first_name='testouille',
			last_name='test',
			email='testouille@testouille.fr')

		self.profil = Profil(name=self.user.username, mailAdress=self.user.email, user=self.user)

		self.assertEquals(self.profil.name, 'testouille')
		self.assertEquals(self.profil.mailAdress, 'testouille@testouille.fr')
		