from django.db import models  #This might be from django import models
import datetime
import PIL


# python manage.py makemigrations in console

# Product Categories
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name

    # Fixes a weird tendency in Django to add an "s" to the end
    # of the plural of a model
    class Meta:
        verbose_name_plural = "Categories"


# Customers
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    date_added = models.DateTimeField(default=datetime.datetime.now)


def __str__(self):
    return f"{self.first_name} {self.last_name}"


#All of our products
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, blank=True, default=True)
    image = models.ImageField(upload_to='uploads/product/')
    #Add sale stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


#customer Orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default="", blank=True)
    email = models.EmailField(max_length=100)
    phone = models.EmailField(max_length=20, default="", blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
