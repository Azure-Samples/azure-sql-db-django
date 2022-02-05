#Serializer for converting complex objects into native Python datatypes and deserialize parsed data back into complex types

from rest_framework import serializers
from customerapi.models import Customer,Product,OrderDetail

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('CustomerId','CustomerName')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product 
        fields=('ProductId','ProductName')

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderDetail 
        fields=('OrderId','CustomerId','ProductId','OrderDate')