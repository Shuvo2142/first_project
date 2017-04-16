from django.contrib import admin

# Register your models here.

from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
	list_display = ["__str__", "price"]
	search_fields = ["title"]

	class meta:
		model= Product



class CategoryAdmin(admin.ModelAdmin):
	list_display = ["__str__", "timestamp"]
	search_fields = ["title"]

	class meta:
		model= Category		


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
