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