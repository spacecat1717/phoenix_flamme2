from django.db import models
from main.models import Item

class Order(models.Model):
    """user's data"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=350)
    postal_code = models.CharField(max_length=20)
    comment = models.CharField(max_length=350)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    track = models.CharField(max_length=200)
    delivery_price = models.PositiveIntegerField(default=300)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    


class OrderItem(models.Model):
        """order items data"""
        order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
        product = models.ForeignKey(Item, related_name='order_items', on_delete=models.CASCADE)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        quantity = models.PositiveIntegerField(default=1)
        oil = models.BooleanField(default=False)
        total_price = models.IntegerField()

        def __str__(self):
            return '{}'.format(self.id)

    