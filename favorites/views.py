from django.shortcuts import render

from .forms import *

# Create your views here.
def addToFavorite(request):
	favoritesForm = FavoriteForm()

	template = 'pages/index.html'

	print("super")
	if request.method == 'POST':
		favoritesForm = FavoriteForm(request.POST)

		print("1")

		if favoritesForm.is_valid():
			print("2")
			productName = request.POST.get('productName')
			substituteName = request.POST.get('substituteName')

			print("3")
			if productName != None and substituteName != None:
				print(productName)
				print(substituteName)

	return render(request, template, locals())