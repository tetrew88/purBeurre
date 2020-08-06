#!/usr/bin/python3

from django import forms


class IdentificationForm(forms.Form):
	mail = forms.EmailField(
		label = "adresse mail",
		max_length=100,
		widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
    )

	password = forms.CharField(
		label='mot de passe',
		max_length=100,
		widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )