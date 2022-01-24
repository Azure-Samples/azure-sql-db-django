#Design your URL route here

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


#URLConf
urlpatterns=[
    path('Customer/', views.CustomerAPI, name="Customer"),
    path('Product/', views.ProductAPI,),
    path('OrderDetails/', views.OrderDetailAPI)
]