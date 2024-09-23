from django.contrib import admin
from . models import order,orderditem
# Register your models here.



@admin.register(order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ['owner__user__username', 'id']
    list_display = ('id', 'owner', 'total_cart_amount', 'order_status', 'created_at', 'delete_status')
    list_filter = ('order_status', 'delete_status', 'created_at')

  



  # Optionally, if you want to format the total cart amount, you can do something like this
    def total_cart_amount(self, obj):
        return f"RS. {obj.total_cart_amount():.2f}"  # Format as a currency
    
    
class OrderedItemAdmin(admin.ModelAdmin):
    search_fields = ['product__title', 'owner__owner__user__username']  # Search by product name and order owner's username
    list_display = ['id', 'product', 'quantity', 'owner']  # Show relevant fields in list view
    list_filter = ['product']  # Filter by product

admin.site.register(orderditem, OrderedItemAdmin)