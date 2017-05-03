from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin

# Create your views here.

from products.models import Product
from sellingcarts.models import SellingCart, SellingCartItem

from sellingcarts.utils.selling_cart_status import SellingCartStatusEnum


class SellingCartConfirmationView(SingleObjectMixin, View):
    model = SellingCart
    template_name = "carts/view.html"

    def get_object(self, *args, **kwargs):
        self.request.session.set_expiry(0)  # when the web browser is closed
        cart_id = self.request.session.get("cart_id")
        # cart = super(SellingCartView, self).get_object(*args, **kwargs)
        if cart_id == None:
            cart = SellingCart()
            cart.save()
            cart_id = cart.id
            self.request.session["cart_id"] = cart_id
        # cart = SellingCart.objects.get(id=cart_id)**********to bound to the seller
        cart = SellingCart.objects.get(id=cart_id)  # user=self.request.user
        # cart.save()
        # ********************************can be changed
        return cart

    def get(self, request, *args, **kwargs):
        cart = self.get_object()
        # cart = super(SellingCartView, self).get_object(*args, **kwargs)

        all_selling_cart_items = SellingCartItem.objects.filter(cart=cart)
        for cart_item in all_selling_cart_items:
            product = Product.objects.get(pk=cart_item.item_id)
            try:
                product.inventory -= cart_item.quantity
                if product.inventory < 0:
                    product.inventory = 0
                product.save()
            except:
                pass
        cart.status = SellingCartStatusEnum.Completed.value
        cart.save()
        return redirect(reverse('inventory_list_view'))
