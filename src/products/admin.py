from django.contrib import admin

# Register your models here.

from .models import Product

class ProductAdmin(admin.ModelAdmin):
	list_display = ["__str__", "price"]

	class meta:
		model= Product


admin.site.register(Product, ProductAdmin)
