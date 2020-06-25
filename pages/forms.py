#!/usr/bin/python3

from django import forms


class IdentificationForm(forms.Form):
	mail = forms.CharField(
		label = "mailAdress",
		max_length=100,
		widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
    )

	password = forms.CharField(
		label='password',
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )