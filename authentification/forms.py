#!/usr/bin/python3

from django import forms


class IdentificationForm(forms.Form):
	mail = forms.CharField(
		label='Mail',
		max_length=100,
		widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True)

	password = forms.CharField(
		label='mot de passe',
		max_length=100,
		widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True)


class RegisterForm(forms.Form):
	name = forms.CharField(
        label='Pseudo',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True)

	mail = forms.EmailField(
		label='adresse mail',
		max_length=100,
		widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True)

	password = forms.CharField(
		label='mot de passe',
		max_length=100,
		widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True)