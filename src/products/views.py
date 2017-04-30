from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

# Create your views here. 

from projectinventory.mixins import LoginRequiredMixin 
from sellers.mixins import SellerAccountMixin

# from projectinventory.mixins import LoginRequiredMixin

from .forms import ProductAddForm, ProdutModelForm, CategoryModelForm
from .models import Product, Category

class CategoryCreateView(SellerAccountMixin, CreateView):
	model = Category	
	template_name = "categories/category_form.html"
	form_class = CategoryModelForm
	success_url = "/categories/create/"

	def form_valid(self, form):
		seller = self.get_account()
		form.instance.seller = seller
		valid_data = super(CategoryCreateView, self).form_valid(form)
		return valid_data	



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



class ProductCreateView(SellerAccountMixin, CreateView):
	model = Product	
	template_name = "products/product_form.html"
	form_class = ProdutModelForm
	success_url = "/seller/products/"

	def form_valid(self, form):
		seller = self.get_account()
		form.instance.seller = seller
		valid_data = super(ProductCreateView, self).form_valid(form)
		return valid_data



class ProductUpdateView(SellerAccountMixin, UpdateView):
	model = Product
	template_name = "products/product_update_form.html"
	form_class = ProdutModelForm
	success_url = "/seller/products/"

	def form_valid(self, form):
		seller = self.get_account()
		form.instance.seller = seller
		valid_data = super(ProductUpdateView, self).form_valid(form)
		return valid_data
	# have to think about it
	def get_context_data(self, *args, **kwargs):
		context = super(ProductUpdateView, self).get_context_data(*args, **kwargs)
		context["submit-btn"] = "Update Product"
		return context			



class SellerProductListView(SellerAccountMixin, ListView):
	model = Product
	queryset = Product.objects.all()
	template_name = "sellers/product_list_view.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SellerProductListView, self).get_context_data(*args, **kwargs)
		return context	



class SellerInventoryListView(SellerAccountMixin, ListView):
	model = Product
	queryset = Product.objects.all()
	template_name = "sellers/inventory_list_view.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SellerInventoryListView, self).get_context_data(*args, **kwargs)
		return context			



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
