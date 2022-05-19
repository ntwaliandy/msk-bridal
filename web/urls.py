from os import name
from django.urls import path, re_path
from . import views
app_name = 'web'
urlpatterns = [
	path('', views.index, name='index'),
	re_path(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
	re_path(r'^category/(?P<category_id>[0-9]+)/$', views.shop, name='shop'),
	re_path(r'^(?P<product_id>[0-9]+)/checkout/$', views.checkout, name='checkout'),
	path('contact/', views.contact, name='contact'),
	path('about/', views.about, name='about')

]