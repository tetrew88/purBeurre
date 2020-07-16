from django.template import loader

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.shortcuts import render 

import requests

from .forms import IdentificationForm

def index(request):
	form = IdentificationForm()

	template = 'pages/index.html'
	return render(request, template, locals())


def account(request):
	template = loader.get_template('pages/account.html')
	return HttpResponse(template.render(request=request))


def connexion(request):
	form = IdentificationForm()

	template = 'pages/index.html'

	if request.method == 'POST':
		form = IdentificationForm(request.POST)

		if form.is_valid():

			username = request.POST.get('mail')
			password = request.POST.get('password')

			print("user: " + username)
			print("password: " + password)

			print('connecter')

			"""
				user = authenticate(username='john', password='secret')

				if user is not None:
					pass
    			else:
    				pass
    		"""
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

			print("Inscrit")
			
			"""
				user = authenticate(username=username, password=password)
			
				if user is not None:
					print("inscrit")
				else:
			    	print("erreur lors de l'inscription")
			"""

		else:
			print("Erreur dans le forulaire d'inscription")

	else:
		pass

	return render(request, template, locals())

