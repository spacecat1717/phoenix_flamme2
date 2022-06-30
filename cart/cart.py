from decimal import Decimal
from django.conf import settings
from main.models import Item



class Cart(object):

    def __init__(self, request):
        """
        initialize cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, item, quantity=1, update_quantity=False):
        """
        Add product to cart and update its quantity
        """
        product_id = str(item.id)
        if product_id not in self.cart:
                self.cart[product_id] = {'quantity': 0,
                                 'price': item.price}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity    
        self.save()

    def save(self):
        # update session
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, item):
        """
        Delete product from cart
        """
        product_id = str(item.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Execution products' data from db
        """
        product_ids = self.cart.keys()
        products = Item.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Counting products in cart
        """
        return sum(item['quantity'] for item in self.cart.values())


    def get_total_price(self):
        """
        Counting price for products in cart
        """
        delivery_price = 300
        return sum(item['price'] * item['quantity'] for item in
                self.cart.values()) + delivery_price 

    def clear(self):
        """Delete cart from session"""
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True    