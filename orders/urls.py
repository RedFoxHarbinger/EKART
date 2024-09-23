
from django.urls import path
from . import views

urlpatterns = [

     
       path('cart/', views.cart,name="cart"),
       path('addtocart/', views.add_to_cart,name="addtocart"),
       path('deletecart/<pk>', views.delete_item,name="deleteitem"),
       path('checkout', views.checkout,name="checkout"),
       path('orders', views.orders,name="orders"),

      
     
]