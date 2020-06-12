from django.template import loader
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

import requests

def index(request):
    template = loader.get_template('pages/index.html')
    return HttpResponse(template.render(request=request))

def connexion(request):
	user = authenticate(username='john', password='secret')

	#if user is not None:
	#	pass
    #else:
    #	pass*/

def inscription(request):
	user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

