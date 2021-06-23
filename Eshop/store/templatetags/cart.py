from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    Keys = cart.keys()
    for id in Keys:
        print("---------------------------",id , Keys)
        print(type(id) , type(product.id))
        if int(id) == product.id:
            return True
        else:
            return False
    return False;

@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    Keys = cart.keys()
    for id in Keys:
        print(id , Keys)
        print(type(id) , type(product.id))
        if int(id) == product.id:
            return cart.get(id)
    return 0;

