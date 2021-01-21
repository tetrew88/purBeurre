from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=100, null=False, unique=True)
	url = models.URLField()


class Product(models.Model):
	name = models.CharField(max_length=100, null=False, unique=True)
	ingredients = models.TextField()
	label = models.CharField(max_length=100)
	saturatedFat = models.CharField(max_length=100)
	fat = models.CharField(max_length=100)
	salt = models.CharField(max_length=100)
	sugar = models.CharField(max_length=100)
	allergen = models.TextField()
	nutriscore = models.CharField(max_length=100)
	url = models.URLField()
	pictureUrl = models.URLField()

	category = models.ManyToManyField(Category, related_name='category')