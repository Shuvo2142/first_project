from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

from sellers.models import SellerAccount


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        return self.get_queryset().active()


class Product(models.Model):
    seller = models.ForeignKey(SellerAccount)
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    sale_price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(null=True, blank=True)  # the inventory is unlimited...i have to change that

    # slug
    # inventory

    # categories = models.ManyToManyField("Category")
    # default = models.ForeignKey("Category", related_name="default_category", null=True, blank=True)
    categories = models.ForeignKey("Category")

    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_price(self):
        if self.sale_price is not None:
            return self.sale_price
        else:
            return self.price

    def get_absolute_url(self):
        return reverse("product_detail_view", kwargs={"pk": self.pk})

    def add_to_cart(self):
        return "%s?item=%s&qty=1" % (reverse("cart"), self.id)

    def remove_from_cart(self):
        return "%s?item=%s&qty=1&delete=True" % (reverse("cart"), self.id)

    def product_update(self):
        return reverse("product_update_view", kwargs={"pk": self.pk})

    def product_delete(self):
        return reverse("product_delete_view", kwargs={"pk": self.pk})

        # def delete(self):
        # 	# return "%s?id=%s&delete=True" %(reverse("product_list_view"), self.id)
        # 	instance = Product.objects.get(pk=self.id)
        # 	instance.delete()


class Category(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=False)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category_detail_view", kwargs={"pk": self.pk})

    def category_update(self):
        return reverse("category_update_view", kwargs={"pk": self.pk})

        # def get_absolute_url(self):
        # 	return reverse("category_detail", kwargs={"slug": self.slug})

# Product Images

# Product Categories
