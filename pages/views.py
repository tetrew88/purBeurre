from django.shortcuts import render 

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
	return render(request, template, locals())

def legalMention(request):
	identifiantForm = IdentificationForm()
	searchForm = SearchForm()
	
	template = 'pages/legalMention.html'
	return render(request, template, locals())