#Design your URL route here

from django.urls import path, re_path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


#URLConf
urlpatterns=[
    re_path(r'^customer/?$', views.CustomerAPI),
    re_path(r'^customer/([0-9]+)/?$', views.CustomerAPI, name='customer'),

    re_path(r'^product/?$', views.ProductAPI),
    re_path(r'^product/([0-9]+)/?$', views.ProductAPI, name='product'),

    re_path(r'^orderdetail/?$', views.OrderDetailAPI),
    re_path(r'^orderdetail/([0-9]+)/?$', views.OrderDetailAPI, name='orderdetail')
]