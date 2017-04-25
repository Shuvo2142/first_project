from django.contrib import admin

# Register your models here.

from .models import SellingCart, SellingCartItem

class SellingCartItemInline(admin.TabularInline):
	model = SellingCartItem



class SellingCartAdmin(admin.ModelAdmin):
	inlines = [
		SellingCartItemInline
	]

	class Meta:
		model = SellingCart

admin.site.register(SellingCart, SellingCartAdmin)
