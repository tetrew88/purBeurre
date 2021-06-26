#!/usr/bin/python3

from django import forms


class FavoriteForm(forms.Form):
	productName = forms.CharField(
		label='product name',
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}),
		required=True
	)

	substituteName = forms.CharField(
		label='substitute name',
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}),
		required=True
	)