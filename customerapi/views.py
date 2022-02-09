#View which takes a request and returns a response

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
#from django.http import HttpResponse

from customerapi.models import Customer, Product, OrderDetail
from customerapi.serializers import CustomerSerializer,ProductSerializer, OrderDetailSerializer


# Create your views here.
#Request handler which takes requests and sends the response

@csrf_exempt
def CustomerAPI (request, id=0):
    if (request.method=='GET' and int(id) > 0):
        customer=Customer.objects.filter(CustomerId=id)
        customer_serializer=CustomerSerializer(customer, many=True)
        return JsonResponse(customer_serializer.data,safe=False)
    elif request.method=='GET':   
        customers = Customer.objects.all()
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
            customer=Customer.objects.get(CustomerId=customer_data['CustomerId'])
            customers_serializer=CustomerSerializer(customer,data=customer_data)
            if customers_serializer.is_valid():
                customers_serializer.save()
                return JsonResponse("Record Updated Successfully",safe=False)
            return JsonResponse("There is some error updating the record", safe=False)
    elif request.method=='DELETE':
        customer=Customer.objects.get(CustomerId=id)
        customer.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)

@csrf_exempt
def ProductAPI (request, id=0):
    if (request.method=='GET' and int(id) > 0):
        product=Product.objects.filter(ProductId=id)
        product_serializer=ProductSerializer(product, many=True)
        return JsonResponse(product_serializer.data,safe=False)
    elif request.method=='GET':
        products =  Product.objects.all()
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
        product=Product.objects.get(ProductId=product_data['ProductId'])
        products_serializer=ProductSerializer(product,data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Record Updated Successfully",safe=False)
        return JsonResponse("There is some error updating the record",safe=False)
    elif request.method=='DELETE':
        product=Product.objects.get(ProductId=id)
        product.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)

@csrf_exempt
def OrderDetailAPI (request, id=0):
    if (request.method=='GET' and int(id) > 0):
        orderDetail=OrderDetail.objects.filter(OrderId=id)
        orderDetail_serializer=OrderDetailSerializer(orderDetail, many=True)
        return JsonResponse(orderDetail_serializer.data,safe=False)
    elif request.method=='GET':
        orderDetails = OrderDetail.objects.all()
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
        orderDetails=OrderDetail.objects.get(OrderId=orderDetails_data['OrderId'])
        orderDetails_serializer=OrderDetailSerializer(orderDetails,data=orderDetails_data)
        if orderDetails_serializer.is_valid():
            orderDetails_serializer.save()
            return JsonResponse("Record Updated Successfully",safe=False)
        return JsonResponse("There is some error updating the record",safe=False)
    elif request.method=='DELETE':
        orderDetails=OrderDetail.objects.get(OrderId=id)
        orderDetails.delete()
        return JsonResponse("Record Deleted Successfully",safe=False)