from django.shortcuts import render

# Create your views here.
def addToFavorite(request, productId):
	print("id:" + productId)