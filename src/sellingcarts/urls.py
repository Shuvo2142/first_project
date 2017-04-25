from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import SellingCartView

urlpatterns = [
	# url(r'^$', 'products.views.home', name='home')
    url(r'^$', SellingCartView.as_view(), name='cart'),
    # url(r'^(?P<pk>\d+)$', SellingCartView.as_view(), name='cart'),
] 