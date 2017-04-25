from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin

# Create your views here.

from products.models import Product
from sellingcarts.models import SellingCart, SellingCartItem


class SellingCartView(SingleObjectMixin, View):
	model = SellingCart
	template_name = "carts/view.html"

	def get_object(self, *args, **kwargs):
		self.request.session.set_expiry(0) # when the web browser is closed
		cart_id = self.request.session.get("cart_id")
		# cart = super(SellingCartView, self).get_object(*args, **kwargs)
		if cart_id == None:
			cart = SellingCart()
			cart.save()
			cart_id = cart.id
			self.request.session["cart_id"] = cart_id
		# cart = SellingCart.objects.get(id=cart_id)**********to bound to the seller
		cart = SellingCart.objects.get(id=cart_id) # user=self.request.user
			# cart.save()
		# ********************************can be changed
		return cart		

	def get(self, request, *args, **kwargs):
		cart = self.get_object()
		# cart = super(SellingCartView, self).get_object(*args, **kwargs)
		item_id = request.GET.get("item")
		delete_item = request.GET.get("delete")
		if item_id:
			item_instance = get_object_or_404(Product, id=item_id)
			qty = request.GET.get("qty", 1)
			try:
				if int(qty) < 1:
					delete_item = True
			except:
				raise Http404
			cart_item = SellingCartItem.objects.get_or_create(cart=cart, item=item_instance)[0]
			if delete_item:
				cart_item.delete()
			else:	
				cart_item.quantity = qty
				cart_item.save()
		context = {
			"object": self.get_object()
		}
		template = self.template_name		
		return render(request, template, context)



	# def get(self, request, *args, **kwargs):
	# 	self.request.session.set_expiry(0)
	# 	cart_id = self.request.session.get("cart_id")
	# 	if cart_id == None:
	# 		cart = SellingCart()
	# 		cart.save()
	# 		cart_id = cart.id
	# 		self.request.session["cart_id"] = cart_id
	# 	if cart_id == None:
	# 		cart = SellingCart()
	# 		cart.save()
	# 		cart_id = cart.id
	# 		self.request.session["cart_id"] = cart_id			
	# 	cart = SellingCart.objects.get(id=cart_id)
	# 	cart.save()	
	# 	item_id = self.request.GET.get("item")
	# 	delete_item = self.request.GET.get("delete")
	# 	if item_id:
	# 		item_instance = get_object_or_404(Product, id=item_id)
	# 		qty = self.request.GET.get("qty")
	# 		cart_item = SellingCartItem.objects.get_or_create(cart=cart, item=item_instance)[0]
	# 		if delete_item:
	# 			cart_item.delete()
	# 		else:	
	# 			cart_item.quantity = qty
	# 			cart_item.save()
	# 	context = {
	# 		# "object": self.get_object()
	# 		"cart": cart
	# 	}
	# 	template = self.template_name		
	# 	return render(request, template, context)	
	# 	# return HttpResponseRedirect("/seller/")			
