from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Product

class ProductListView(ListView):
	model = Product
	queryset = Product.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		return context

	# def get_queryset(self, *args, **kwargs):
	# 	product_pk = self.kwargs.get("pk")

	# def post(self, request, *args, **kwargs):
		



class ProductDetailView(DetailView):
	model = Product
