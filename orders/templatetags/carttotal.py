from django import template

register=template.Library()

@register.simple_tag(name='carttotal')
def carttotal(cart):
    total=0
    for item in cart.added_items.all():
        total+=item.product.price*item.quantity
    return total       

    """return sum(item.product.price * item.quantity for item in cart.added_items.all() if item.product.price is not None)"""