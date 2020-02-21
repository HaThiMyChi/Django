from django.db import models

# Create your models here.

# Danh muc
class Category(models.Model):
	# cai id no tu sinh khong can phai khai bao
	title = models.CharField(default='', max_length='')
	slug = models.CharField(max_length=100, default='')
	description = models.TextField(default='')
	active = models.BooleanField(default=True)
	

class Product(models.Model):
	title = models.CharField(max_length=255, default='')
	description = models.TextField(default='')
	# do category lien ket voi bang Category nen no la khoa ngoai nen khai bao de lien ket
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	price = models.IntegerField(default=0)
	active = models.BooleanField(default= True)

class Variation(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	title = models.CharField(max_length=255, default='')
	price = models.IntegerField(default=0)
	sale_price = models.IntegerField(default=0)
	inventory = models.IntegerField(default=0)
	active = models.BooleanField(default=True)