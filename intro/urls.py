from django.urls import path
from . import views

urlpatterns = [
    path ('' , views.index , name = 'index'),
    path ('product_detail/',views.product_detail , name = 'product_detail'),
    path ('cart/',views.cart , name = 'cart'),
    path ('products/',views.products , name = 'products'),
    path ('checkout/', views.checkout , name = 'checkout'),
    path ('contact/', views.contact , name = 'contact'),
    path ('register/', views.register , name = 'register')
]