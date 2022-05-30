from django.db import models
from django.conf import settings


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
    title = models.CharField(max_length = 150)
    description = models.CharField(max_length = 250)
    text = models.TextField()
    price = models.IntegerField()
    photo1 = models.ImageField(upload_to = 'static/')
    photo2 = models.ImageField(upload_to = 'static/')
    small = False #need to add small list what will save in cart
    def __str__(self):
        return self.title

class Topic(models.Model):
    """Class for topic"""
    title = models.CharField(max_length = 200)
    text = models.TextField()
    photo = models.ImageField(upload_to = 'static/')
    def __str__(self):
        return self.title