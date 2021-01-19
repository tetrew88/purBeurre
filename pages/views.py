from django.shortcuts import render
from django.http import HttpResponse

from .forms import *

def index(request):
	identifiantForm = IdentificationForm()
	searchForm = SearchForm()

	template = 'pages/index.html'

	return render(request, template, locals())


def account(request):
	identifiantForm = IdentificationForm()
	searchForm = SearchForm()

	template = 'pages/account.html'

	if request.user.is_authenticated:
		return render(request, template, locals())
	else:
		return HttpResponse('Unauthorized', status=401)

def legalMention(request):
	identifiantForm = IdentificationForm()
	searchForm = SearchForm()
	
	template = 'pages/legalMention.html'
	return render(request, template, locals())