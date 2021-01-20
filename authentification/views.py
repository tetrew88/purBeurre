from django.template import loader
from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.shortcuts import redirect

from substitutesearch.management.commands.databaseFunction import searchProfil

from .forms import *
from .models import *

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.core.exceptions import MultipleObjectsReturned

UserModel = get_user_model()

class EmailBackend(ModelBackend):
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

	identifiantForm = IdentificationForm()

	template = '/'

	if request.method == 'POST':
		identifiantForm = IdentificationForm(request.POST)

		if identifiantForm.is_valid():

			mail = request.POST.get('mail')
			password = request.POST.get('password')

			user = EmailBackend().authenticate(request, username=mail, password=password)

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