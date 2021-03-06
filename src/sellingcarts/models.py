from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete

# Create your models here.

from products.models import Product
from sellers.models import SellerAccount

from .utils.selling_cart_status import SellingCartStatusEnum


class SellingCartItem(models.Model):
    cart = models.ForeignKey("SellingCart")
    item = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField(default=1)
    line_item_total = models.DecimalField(decimal_places=2, max_digits=20, null=True)

    def __str__(self):
        return self.item.title

    def remove(self):
        return self.item.remove_from_cart()


def selling_cart_item_pre_save_receiver(sender, instance, *args, **kwargs):
    qty = instance.quantity
    if int(qty) >= 1:
        price = instance.item.get_price()
        line_item_total = Decimal(qty) * Decimal(price)
        instance.line_item_total = line_item_total


pre_save.connect(selling_cart_item_pre_save_receiver, sender=SellingCartItem)


def selling_cart_item_post_save_receiver(sender, instance, *args, **kwargs):
    instance.cart.update_subtotal()


post_save.connect(selling_cart_item_post_save_receiver, sender=SellingCartItem)

post_delete.connect(selling_cart_item_post_save_receiver, sender=SellingCartItem)


class SellingCart(models.Model):
    seller = models.ForeignKey(SellerAccount, null=True, blank=True)
    items = models.ManyToManyField(Product, through=SellingCartItem)
    # quantity = models.PositiveIntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    subtotal = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    status = models.IntegerField(default=SellingCartStatusEnum.Draft.value)

    def __str__(self):
        return str(self.id)

    def update_subtotal(self):
        subtotal = 0
        items = self.sellingcartitem_set.all()
        for item in items:
            subtotal += item.line_item_total
        self.subtotal = subtotal
        self.save()

    # seller
    # items
    # timestamp created
    # updated

    # subtotal price
    # taxes total
    # discounts
    # total price
