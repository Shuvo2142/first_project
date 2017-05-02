from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from products.views import (ProductCreateView,
							ProductUpdateView,
							SellerProductListView,
							CategoryListView,
							CategoryCreateView,
							SellerInventoryListView,
							ProductDetailView,
							CategorytUpdateView,
							CategoryDetailView,
							)

from .views import SellerDashboard

urlpatterns = [
	url(r'^$', SellerDashboard.as_view(), name='dashboard'),
	url(r'^categories/$', CategoryListView.as_view(), name='category_list_view'),
	url(r'^categories/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name='category_detail_view'),
	url(r'^products/$', SellerProductListView.as_view(), name='product_list_view'),
	url(r'^products/create/$', ProductCreateView.as_view(), name='product_create_view'),
	# url(r'^products/update/$', ProductUpdateView.as_view(), name='product_update_view'),
	url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail_view'),
	url(r'^products/(?P<pk>\d+)/update/$', ProductUpdateView.as_view(), name='product_update_view'),
	url(r'^categories/create/$', CategoryCreateView.as_view(), name='category_create_view'),
	url(r'^categories/(?P<pk>\d+)/update/$', CategorytUpdateView.as_view(), name='category_update_view'),
	url(r'^inventory/$', SellerInventoryListView.as_view(), name='inventory_list_view'),
]