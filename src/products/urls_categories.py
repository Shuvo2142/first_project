from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import CategoryListView, CategoryDetailView, CategoryCreateView, CategorytUpdateView

urlpatterns = [
	# url(r'^$', CategoryListView.as_view(), name='categories'),
	# url(r'^(?P<slug>[\w-])/$', CategoryDetailView.as_view(), name='category_detail'),
	# url(r'^create/$', CategoryCreateView.as_view(), name='category_create_view'),
	# url(r'^(?P<pk>\d+)/$', CategoryDetailView.as_view(), name='category_detail'),
	# url(r'^(?P<pk>\d+)/update/$', CategorytUpdateView.as_view(), name='category_update_view'),
]