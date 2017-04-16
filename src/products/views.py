from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Product

class ProductListView(ListView):
	model = Product

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		return context



class ProductDetailView(DetailView):
	model = Product
