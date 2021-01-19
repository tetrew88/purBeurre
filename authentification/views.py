from django.template import loader
from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.shortcuts import redirect

from substitutesearch.management.commands.databaseFunction import searchProfil

from .forms import *
from .models import *

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
			else:
				messages.warning(request, "Erreur lors de l'identification")
		else:
			messages.warning(request, "Erreur lors de l'identification")

	else:
		pass
	

	return redirect(template)


def register(request):
	registerForm = RegisterForm()

	template = 'pages/register.html'

	if request.method == 'POST':
		registerForm = RegisterForm(request.POST)

		if registerForm.is_valid():
			username = request.POST.get('name')
			mail = request.POST.get('mail')
			password = request.POST.get('password')
			
			try:
				user = User.objects.create_user(username, mail, password)
			except:
				if searchProfil(username) == False:
					messages.warning(request, "Mail déja utiliser")
				else:
					messages.warning(request, "Pseudo déja utiliser")
					
				return render(request, template, {'registerForm':registerForm})

			profil = Profil(name = username, mailAdress = mail, user = user)

			profil.save()

			login(request, user)

			return redirect('/', {'registerForm':registerForm})
			

	return render(request, template, {'registerForm':registerForm})


def deconnexion(request):
	template = '/'

	logout(request)

	return redirect(template, locals())