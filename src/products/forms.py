from django import forms

from .models import Product, Category

PUBLISH_CHOICES = (
		('publish' 'Publish'),
		('draft', 'Draft'),
	)


class CategoryModelForm(forms.ModelForm):

	class Meta:
		model = Category
		fields = [
			"title",
			"description",
		]



class ProductAddForm(forms.Form):
	title = forms.CharField()
	# description = forms.TextField(widget=forms.Textarea)
	price = forms.DecimalField()
	publish = forms.ChoiceField(widget= forms.RadioSelect, choices=PUBLISH_CHOICES)

	def clean_price(self):
		price = self.cleaned_data.get("price")
		if price <= 0:
			raise forms.ValidationError("Submit a valid price")
		else:	
			return price



class ProdutModelForm(forms.ModelForm):
	# publish = forms.ChoiceField(widget= forms.RadioSelect, choices=PUBLISH_CHOICES)

	class Meta:
		model = Product
		fields = [
			"title",
			"description",
			"sale_price",
			"price",
			"categories",
			"inventory",
		]

	def clean_price(self):
		price = self.cleaned_data.get("price")
		if price <= 0:
			raise forms.ValidationError("Submit a valid price")
		else:	
			return price


