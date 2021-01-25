from django.shortcuts import render
from django.http import HttpResponse

from authentification.forms import IdentificationForm
from substitutesearch.forms import SearchForm


def index(request):
	""" index pages """

	identifiantForm = IdentificationForm()
	searchForm = SearchForm()

	template = 'pages/index.html'

	return render(request, template, locals())


def account(request):
	""" account pages """
	identifiantForm = IdentificationForm()
	searchForm = SearchForm()

	template = 'pages/account.html'

	if request.user.is_authenticated:
		return render(request, template, locals())
	else:
		return HttpResponse('Unauthorized', status=401)


def legalMention(request):
	""" legal mentions pages """
	identifiantForm = IdentificationForm()
	searchForm = SearchForm()

	template = 'pages/legalMention.html'
	return render(request, template, locals())