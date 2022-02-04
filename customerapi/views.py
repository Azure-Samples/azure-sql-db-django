#View which takes a request and returns a response

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
#from django.http import HttpResponse

from customerapi.models import Customers, Products, OrderDetails
from customerapi.serializers import CustomerSerializer,ProductSerializer, OrderDetailSerializer


# Create your views here.
#Request handler which takes requests and sends the response

@csrf_exempt
def CustomerAPI (request):
    if request.method=='GET':
        
        customers =  Customers.objects.all()
        customers_serializer=CustomerSerializer(customers,many=True)
        return JsonResponse(customers_serializer.data,safe=False)
    elif request.method=='POST':
        customer_data=JSONParser().parse(request)
        customers_serializer=CustomerSerializer(data=customer_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Record Inserted Successfully",safe=False)
        return JsonResponse("Oops...something went wrong.",safe=False)
    elif request.method=='PUT':
        customer_data=JSONParser().parse(request)
        customer=Customers.objects.get(CustomerId=customer_data['CustomerId'])
        customers_serializer=CustomerSerializer(customer,data=customer_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Record Updated Successfully",safe=False)
        return JsonResponse("There is some error updating the record")
    elif request.method=='DELETE':
        customer_data=JSONParser().parse(request)
        customer=Customers.objects.get(CustomerId=customer_data['CustomerId'])
        customer.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)

@csrf_exempt
def ProductAPI (request):
    if request.method=='GET':
        products =  Products.objects.all()
        products_serializer=ProductSerializer(products,many=True)
        return JsonResponse(products_serializer.data,safe=False)
    elif request.method=='POST':
        product_data=JSONParser().parse(request)
        products_serializer=ProductSerializer(data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Record Inserted Successfully",safe=False)
        return JsonResponse("Oops...something went wrong.",safe=False)
    elif request.method=='PUT':
        product_data=JSONParser().parse(request)
        product=Products.objects.get(ProductId=product_data['ProductId'])
        products_serializer=ProductSerializer(product,data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Record Updated Successfully",safe=False)
        return JsonResponse("There is some error updating the record")
    elif request.method=='DELETE':
        product_data=JSONParser().parse(request)
        product=Products.objects.get(ProductId=product_data['ProductId'])
        product.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)

@csrf_exempt
def OrderDetailAPI (request):
    if request.method=='GET':
        orderDetails =  OrderDetails.objects.all()
        orderDetails_serializer=OrderDetailSerializer(orderDetails,many=True)
        return JsonResponse(orderDetails_serializer.data,safe=False)
    elif request.method=='POST':
        orderDetails_data=JSONParser().parse(request)
        orderDetails_serializer=OrderDetailSerializer(data=orderDetails_data)
        if orderDetails_serializer.is_valid():
            orderDetails_serializer.save()
            return JsonResponse("Record Inserted Successfully",safe=False)
        return JsonResponse("Oops...something went wrong.",safe=False)
    elif request.method=='PUT':
        orderDetails_data=JSONParser().parse(request)
        orderDetails=OrderDetails.objects.get(OrderId=orderDetails_data['OrderId'])
        orderDetails_serializer=OrderDetailSerializer(orderDetails,data=orderDetails_data)
        if orderDetails_serializer.is_valid():
            orderDetails_serializer.save()
            return JsonResponse("Record Updated Successfully",safe=False)
        return JsonResponse("There is some error updating the record")
    elif request.method=='DELETE':
        orderDetails_data=JSONParser().parse(request)
        orderDetails=OrderDetails.objects.get(OrderId=orderDetails_data['OrderId'])
        orderDetails.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)