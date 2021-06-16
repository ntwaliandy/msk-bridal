from os import name
from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'web'
urlpatterns = [
	path('', views.index, name='index'),
	url(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^category/(?P<category_id>[0-9]+)/$', views.shop, name='shop'),
	url(r'^(?P<product_id>[0-9]+)/checkout/$', views.checkout, name='checkout'),
	path('contact/', views.contact, name='contact'),
	path('about/', views.about, name='about')

]