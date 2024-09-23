from django import template

register=template.Library()

@register.simple_tag(name='order_status')
def order_status(STATUS):
    STATUS=STATUS-1
    status_list=['ORDER_CONFIRMED','ORDER_PROCESSED','ORDER_DELIVERED','ORDER_REJECTED']
   
    return status_list[STATUS] 