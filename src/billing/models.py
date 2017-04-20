from django.conf import settings
from django.db import models

# Create your models here.

from products.models import Product


class Transaction(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	product = models.ForeignKey(Product)
	price = models.DecimalField(decimal_places=2, max_digits=20)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	success = models.BooleanField(default=True)

	def __str__(self):
		return "%s" %(self.id)
