#!/usr/bin/python3

from django import forms
from favorites.forms import *


class SearchForm(forms.Form):
	keyword = forms.CharField(
		label='Rechercher',
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}),
		required=True
	)