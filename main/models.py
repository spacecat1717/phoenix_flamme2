from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


"""Basic models"""

class Category(models.Model):
    """Class for categories of items"""
    title = models.CharField(max_length = 200)
    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.title

class Item(models.Model):
    """Class for item"""
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    text = models.TextField()
    price = models.IntegerField(default=100)
    photo1 = models.ImageField(upload_to = 'static/')
    photo2 = models.ImageField(upload_to = 'static/')
    #Добавлено для формы отправки в корзину
    quantity = models.IntegerField(default=1)
    small = models.CharField(max_length=20)  
    def __str__(self):
        return self.title

"""Cart models"""

class Cart(models.Model):
    """Class for cart"""
    title = models.CharField(max_length = 100)
    def __str__(self):
        return self.title

class CartItem(Item):
    """Class for items that added to cart"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    def __str__(self):
        return self.item_num

"""Topics models"""

class Topic(models.Model):
    """Class for topic"""
    title = models.CharField(max_length = 200)
    text = models.TextField()
    photo = models.ImageField(upload_to = 'static/')
    def __str__(self):
        return self.title

