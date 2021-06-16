from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Category, Product
from django.conf import settings
from django.contrib.auth.models import User
# Create your views here.

def index(request):
	all_categories = Category.objects.all()
	all_products = Product.objects.all()
	context = {
		'all_categories': all_categories,
		'all_products': all_products
	}
	return render(request, 'index.html', context)

def detail(request, product_id):
	products = get_object_or_404(Product, pk=product_id)
	context = {
		
		'products': products
	}
	return render(request, 'shop-detail.html', context)

def shop(request, category_id):
	categories = get_object_or_404(Category, pk=category_id)
	context = {
		'categories': categories
	}
	return render(request, 'shop.html', context)

def checkout(request, product_id):
	
	products = get_object_or_404(Product, pk=product_id)
	context = {
		
		'products': products
	}
	return render(request, 'checkout.html', context)


def contact(request):
	all_categories = Category.objects.all()
	context = {
		'all_categories': all_categories
	}
	return render(request, 'contact-us.html', context)

def about(request):
	all_categories = Category.objects.all()
	context = {
		'all_categories': all_categories
	}
	return render(request, 'about.html', context)