from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from django.shortcuts import redirect

from django.db.utils import IntegrityError
from django.db.models import Q
from django.core.exceptions import MultipleObjectsReturned

from substitutesearch.management.commands.database_function import search_profil
from substitutesearch.forms import SearchForm

from .forms import IdentificationForm, RegisterForm
from .models import Profil


UserModel = get_user_model()


class EmailBackend(ModelBackend):
	""" class for identify an user by his mail """

	def authenticate(self, request, username=None, password=None, **kwargs):
		try:
			user = UserModel.objects.get(
				Q(username__iexact=username) | Q(email__iexact=username))
		except UserModel.DoesNotExist:
			UserModel().set_password(password)
		except MultipleObjectsReturned:
			return User.objects.filter(email=username).order_by('id').first()
		else:
			if user.check_password(password) and self.user_can_authenticate(user):
				return user

	def get_user(self, user_id):
		try:
			user = UserModel.objects.get(pk=user_id)
		except UserModel.DoesNotExist:
			return None

		return user if self.user_can_authenticate(user) else None


def connexion(request):
	""" 
		view allowing a user to identify himself:
			1)collect mail and password from identification form.
			2)use personnal class for identification
				if identification is succes return the use to index.
				else signal the error to the user.
	"""

	identifiantForm = IdentificationForm()

	template = '/'

	if request.method == 'POST':
		identifiantForm = IdentificationForm(request.POST)

		if identifiantForm.is_valid():
			""" collect mail an password """
			mail = request.POST.get('mail')
			password = request.POST.get('password')

			""" use personnal identification class for identification"""
			user = EmailBackend().authenticate(request, username=mail, password=password)

			if user is not None:
				""" if user is authentificated log him"""
				login(request, user)
			else:
				""" else signal error to user """
				messages.warning(request, "Erreur lors de l'identification")
		else:
			messages.warning(request, "Erreur lors de l'identification")

	else:
		pass

	return redirect(template)


def register(request):
	""" 
		view allowing a visitor to register himself:
			1)collect name, mail and password from register form.
			2)account/profil creation
				try to create a user and a profil
					if an integrity error occurs
						test if the username/mail was already use
						signal error to visitor and redirect him to register pages
					if succes
						redirect user to index
	"""
	registerForm = RegisterForm()

	template = 'pages/register.html'

	if request.method == 'POST':
		registerForm = RegisterForm(request.POST)

		if registerForm.is_valid():
			""" collect name, mail and password """
			username = request.POST.get('name')
			mail = request.POST.get('mail')
			password = request.POST.get('password')

			try:
				""" Try to create user and profil """

				user = User.objects.create_user(username, mail, password)

				profil = Profil(name=username, mailAdress=mail, user=user)

				profil.save()

				login(request, user)

				return redirect('/', {'identifiantForm': IdentificationForm(), 'searchForm': SearchForm()})

			except IntegrityError:
				""" if an integritty error occurs """
				registerForm = RegisterForm()

				""" test if username or mail was already use and signal error to user """
				if search_profil(username):
					messages.warning(request, "Pseudo déja utiliser")
				else:
					messages.warning(request, "Mail déja utiliser")

				return render(request, template, {'registerForm': registerForm, 'identifiantForm': IdentificationForm(), 'searchForm': SearchForm()})

	return render(request, template, {'registerForm': registerForm, 'identifiantForm': IdentificationForm(), 'searchForm': SearchForm()})


def deconnexion(request):
	""" deconnect user """
	template = '/'

	logout(request)

	return redirect(template, locals())