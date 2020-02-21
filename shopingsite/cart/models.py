from django.db import models
import product.models import Variation

# Create your models here.

class Cart(models.Model):
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)
	
	
class CartItem(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	item = models.ForeignKey(Variation, on_delete=models.CASCADE)