from django.core.exceptions import RequestAborted
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# from django.contrib import messages,auth
# from django.contrib.auth.decorators import login_required
# from shops.models import Shop


# Create your models here.
# from cats.models import Cats
# from products.models import Products

class Supplier(models.Model):
    sup_name = models.CharField(max_length = 256, blank=False)    
    contactperson = models.CharField(max_length = 256, blank=False)    
    contactno = models.CharField(max_length = 24, blank=False)    
    location = models.CharField(max_length = 999, blank=False)   
    date = models.DateTimeField(default=datetime.now, blank=True)    
    def __str__(self):
        return self.sup_name

class Shop(models.Model):
    shopname = models.CharField(max_length = 256, blank=False)    
    owner = models.CharField(max_length = 256, blank=False)    
    contactno = models.CharField(max_length = 24, blank=False)    
    location = models.CharField(max_length = 999, blank=False)   
    date = models.DateTimeField(default=datetime.now, blank=True)    
    def __str__(self):
        return self.shopname

class Product(models.Model):
    product_name = models.CharField(max_length = 256, blank=False)    
    comp_price = models.DecimalField(max_digits = 19, decimal_places=  2)
    price = models.DecimalField(max_digits = 19, decimal_places=  2)
    qty = models.IntegerField(default=1)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)    
    def __str__(self):
        return self.product_name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    emp = models.ForeignKey(User, on_delete=models.CASCADE) 
    date = models.DateTimeField(default=datetime.now, blank=True)  
    def __str__(self):
        return self.product_id  

class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)    
    emp = models.ForeignKey(User, on_delete=models.CASCADE) 
    qty = models.IntegerField(default=1)
    date = models.DateTimeField(default=datetime.now, blank=True)  
    def __str__(self):
        return self.order_id  

class Author(models.Model):
   name = models.CharField(max_length=100)

class Book(models.Model):
   author = models.ForeignKey(Author, on_delete=models.CASCADE)
   title = models.CharField(max_length=100)

class Person(models.Model):
    name = models.CharField(max_length=128)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person)

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)