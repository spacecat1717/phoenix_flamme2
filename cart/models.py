from django.db import models
from main.models import Item
from datetime import datetime

class Cart(models.Model):
    title = models.CharField(max_length = 100)
    def __str__(self):
        return self.title

class CartItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    def __str__(self):
        return  self.client + " - " + self.product