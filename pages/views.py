from django.shortcuts import render 

from .forms import *

def index(request):
	identifiantForm = IdentificationForm()
	searchForm = SearchForm

	template = 'pages/index.html'
	return render(request, template, locals())


def account(request):
	template = loader.get_template('pages/account.html')
	return HttpResponse(template.render(request=request))