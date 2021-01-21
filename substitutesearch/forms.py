#!/usr/bin/python3

from django import forms


class SearchForm(forms.Form):
	keyword = forms.CharField(
		label='Rechercher',
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}),
		required=True
	)


class DetailForm(forms.Form):
	keyword = forms.CharField(
		label='detail',
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}),
		required=True
	)