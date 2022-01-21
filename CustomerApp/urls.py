from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

#URLConf
urlpatterns=[
    path('Customer/', views.CustomerAPI),
    path('Product/([0-9]+)$', views.ProductAPI),
    path('OrderDetails/', views.OrderDetailAPI)

    # url(r'^Customer$',views.CustomerAPI),
    # url(r'^Customer/([0-9]+)$',views.CustomerAPI)
]