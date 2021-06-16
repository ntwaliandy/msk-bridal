from django.db import models

# Create your models here.
class Category(models.Model):
	category_name = models.CharField(max_length=150)

	def __str__(self):
		return self.category_name

class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	product_name = models.CharField(max_length=250)
	product_photo = models.FileField()
	product_view_1 = models.FileField()
	product_view_2 = models.FileField()
	description = models.TextField(max_length=1000)
	product_size = models.CharField(max_length=10)
	product_price = models.DecimalField(max_digits=6, decimal_places=0)

	def __str__(self):
		return self.product_name + "  -->  " + self.product_size
