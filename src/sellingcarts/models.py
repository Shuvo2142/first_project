from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

from products.models import Product
from sellers.models import SellerAccount

class SellingCartItem(models.Model):
	cart = models.ForeignKey("SellingCart")
	item = models.ForeignKey(Product)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.item.title

	def remove(self):
		return self.item.remove_from_cart()



class SellingCart(models.Model):
	seller = models.ForeignKey(SellerAccount, null=True, blank=True)
	items = models.ManyToManyField(Product, through=SellingCartItem)
	# quantity = models.PositiveIntegerField(default=1)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return str(self.id)
	# seller
	# items
	# timestamp created
	# updated

	# subtotal price
	# taxes total
	# discounts
	# total price

