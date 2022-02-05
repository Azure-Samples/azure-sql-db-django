from django.contrib import admin

from customerapi.models import Customer, OrderDetail, Product

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(OrderDetail)
