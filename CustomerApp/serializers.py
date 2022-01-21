from rest_framework import serializers
from CustomerApp.models import Customers,Products,OrderDetails

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers 
        fields=('CustomerId','CustomerName')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products 
        fields=('ProductId','ProductName')

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderDetails 
        fields=('OrderId','CustomerId','ProductId','OrderDate')