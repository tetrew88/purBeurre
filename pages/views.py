from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

import requests

from .forms import IdentificationForm

def index(request):
    template = loader.get_template('pages/index.html')
    return HttpResponse(template.render(request=request))

def account(request):
	template = loader.get_template('pages/account.html')
	return HttpResponse(template.render(request=request))

"""def connexion(request):
	print("yes")
	if request.method == 'POST':
		form = IdentificationForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('connected')

	#user = authenticate(username='john', password='secret')

	#if user is not None:
	#	pass
    #else:
    #	pass*/

def inscription(request):
	user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')"""

