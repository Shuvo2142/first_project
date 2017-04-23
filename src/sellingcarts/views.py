from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.

from products.models import Product
from sellingcarts.models import SellingCart


class SellingCartView(View):

	def get(self, request, *args, **kwargs):
		item_id = request.GET.get("item")
		if item_id:
			item_instance = get_object_or_404(Product, id=item_id)
			qty = request.GET.get("qty")
			cart = SellingCart.objects.all().first()
			cart_item = SellingCart.objects.get_or_create(cart=cart, item=item_instance)[0]
			cart_item.quantity = 20
			cart_item.save()
		print(cart_item)
		return HttpResponseRedirect("/seller/")
