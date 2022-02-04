#Design your URL route here

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


#URLConf
urlpatterns=[
    path('customer/', views.CustomerAPI, name="customer"),
    path('product/', views.ProductAPI,),
    path('orderdetails/', views.OrderDetailAPI)
]