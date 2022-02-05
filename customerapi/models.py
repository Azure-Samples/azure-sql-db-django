#A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table

from math import fabs
from django.db import models

# Create your models here.

class Customer(models.Model):
    CustomerId = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=500)
    
    def __str__(self):
        return self.CustomerName

class Product(models.Model):
    ProductId = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=500)

    def __str__(self):
        return self.ProductName


class OrderDetail(models.Model):
    OrderId = models.AutoField(primary_key=True)
    CustomerId = models.IntegerField(blank=False)
    ProductId = models.IntegerField(blank=False)
    OrderDate = models.DateField()

    def __str__(self):
        return f"Order #{self.OrderId}"
