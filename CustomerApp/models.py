from django.db import models

# Create your models here.

class Customers(models.Model):
    CustomerId = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=500)

class Products(models.Model):
    ProductId = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=500)

class OrderDetails(models.Model):
    OrderId = models.AutoField(primary_key=True)
    CustomerId = models.IntegerField()
    ProductId = models.IntegerField()
    OrderDate = models.DateField()