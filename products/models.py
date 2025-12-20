from django.db import models

class Category(models.Model):
	name=models.CharField(max_length=100,unique=True)
	slug=models.SlugField(unique=True)
	description=models.TextField(blank=True)
	status=models.BooleanField(default=True)

	def __str__(self):
		return self.name

class SubCategory(models.Model):
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	slug=models.SlugField(unique=True)
	status=models.BooleanField(default=True)

	def __str__(self):
		return f"{self.category.name}->{self.name}"

class Product(models.Model):
	subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	sku=models.CharField(max_length=50,unique=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	stock=models.PositiveIntegerField()
	description=models.TextField(blank=True)
	image=models.ImageField(upload_to='porducts/',blank=True,null=True)

	def __str__(self):
		return self.name