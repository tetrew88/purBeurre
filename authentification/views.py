from django.template import loader
from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import redirect

from .forms import *


def connexion(request):
	identifiantForm = IdentificationForm()

	template = '/'

	if request.method == 'POST':
		identifiantForm = IdentificationForm(request.POST)

		if identifiantForm.is_valid():

			username = request.POST.get('name')
			password = request.POST.get('password')

			user = authenticate(username=username, password=password)

			if user is not None:
				login(request, user)
				print('connecter')
			else:
				print('utilisateur invalide')
		else:
			print("Erreur dans la remise du formulaire de conexion")

	else:
		pass
	

	return redirect(template, locals())


def register(request):
	identifiantForm = RegisterForm()

	template = 'pages/register.html'

	if request.method == 'POST':
		identifiantForm = RegisterForm(request.POST)

		if identifiantForm.is_valid():
			username = request.POST.get('name')
			mail = request.POST.get('mail')
			password = request.POST.get('password')
			
			user = User.objects.create_user(username, mail, password)

			print("Inscrit")

		else:
			print("Erreur dans le forulaire d'inscription")

	else:
		pass

	return render(request, template, locals())


def deconnexion(request):
	template = '/'

	logout(request)

	return redirect(template, locals())