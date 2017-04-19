from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

# Create your views here. 

from .forms import ProductAddForm, ProdutModelForm, CategoryModelForm
from .models import Product, Category

class CategoryCreateView(CreateView):
	model = Category	
	template_name = "categories/category_form.html"
	form_class = CategoryModelForm
	success_url = "/categories/create/"



class CategoryListView(ListView):
	model = Category
	queryset = Category.objects.all()
	template_name = "categories/category_list.html"



class CategoryDetailView(DetailView):
	model = Category
	template_name = "categories/category_detail.html"

#next time for slug
	# def get_object(self, *args, **kwargs):
	# 	obj = super(CategoryDetailView, self).get_object(*args, **kwargs)
	# 	return obj



class ProductCreateView(CreateView):
	model = Product	
	template_name = "products/product_form.html"
	form_class = ProdutModelForm
	success_url = "/products/create/"



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
