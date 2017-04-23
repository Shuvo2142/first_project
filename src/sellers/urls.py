from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from products.views import ProductCreateView, SellerProductListView, CategoryListView, CategoryCreateView

from .views import SellerDashboard

urlpatterns = [
	url(r'^$', SellerDashboard.as_view(), name='dashboard'),
	url(r'^categories/$', CategoryListView.as_view(), name='category_list-view'),
	url(r'^products/$', SellerProductListView.as_view(), name='product_list_view'),
	url(r'^products/create/$', ProductCreateView.as_view(), name='product_create_view'),
	url(r'^categories/create/$', CategoryCreateView.as_view(), name='category_create_view'),
]