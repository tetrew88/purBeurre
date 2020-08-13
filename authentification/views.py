from django.template import loader

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.shortcuts import render 

from .forms import IdentificationForm


def connexion(request):
	identifiantForm = IdentificationForm()

	template = 'pages/index.html'

	if request.method == 'POST':
		identifiantForm = IdentificationForm(request.POST)

		if identifiantForm.is_valid():

			username = request.POST.get('mail')
			password = request.POST.get('password')

			user = authenticate(username=username, password=password)

			if user is not None:
				print('connecter')
			else:
				pass
		else:
			print("Erreur dans la remise du formulaire de conexion")

	else:
		pass
	

	return render(request, template, locals())


def inscription(request):
	form = IdentificationForm()

	template = 'pages/index.html'

	if request.method == 'POST':
		form = IdentificationForm(request.POST)

		if form.is_valid():
			username = request.POST.get('mail')
			password = request.POST.get('password')

			print("user: " + username)
			print("password: " + password)
			
			user = User.objects.create_user(username, username, password)

			print("Inscrit")

		else:
			print("Erreur dans le forulaire d'inscription")

	else:
		pass

	return render(request, template, locals())