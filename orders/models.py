from django.db import models
from customers.models import customer
from products.models import products

# Create your models here.
class order(models.Model):
    class Meta:
         verbose_name_plural ="order"
    LIVE=0
    DELETE=1
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
 
    owner=models.ForeignKey(customer,on_delete=models.SET_NULL,related_name='orders',null=True)
    total_cart_amount=models.FloatField(default=0)
    STATUS_CHOICE=((ORDER_CONFIRMED,'ORDER_CONFIRMED'),(ORDER_PROCESSED,'ORDER_PROCESSED'),(ORDER_DELIVERED,"ORDER_DELIVERED"),(ORDER_REJECTED,'ORDER_REJECTED'))
    DELETE_CHOICES=((LIVE,'LIVE'),(DELETE,'DELETE'))
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



       # Add this method to calculate the cart total
    def total_cart_amount(self):
        total = 0
        for item in self.added_items.all():
            total += item.product.price * item.quantity
        return total
    
    def __str__(self) -> str:
        return "order-{}-{}".format(self.id,self.owner.user.username)
    
    
class orderditem(models.Model):
  
 
    product=models.ForeignKey(products,on_delete=models.SET_NULL,null=True,related_name='added_carts')
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(order,on_delete=models.CASCADE,related_name='added_items')

