from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


"""Basic models"""

class Category(models.Model):
    """Class for categories of items"""
    title = models.CharField(max_length = 200)
    description = models.TextField()
    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.title

class Item(models.Model):
    """Class for items"""
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    text = models.TextField()
    price = models.IntegerField(default=100)
    photo1 = models.ImageField(upload_to = 'media/main/static/')
    photo2 = models.ImageField(upload_to = 'media/main/static/')
    show_on_main = models.BooleanField(default=False)
    class Meta:
        ordering = ('title',)
        
    def __str__(self):
        return self.title

"""Other models"""

class Topic(models.Model):
    """Class for topic"""
    title = models.CharField(max_length = 200)
    text = models.TextField()
    photo = models.ImageField(upload_to = 'media/main/static/')
    def __str__(self):
        return self.title

class Feedback(models.Model):
    """Feedback model"""
    name = models.CharField(max_length=100)
    text = models.TextField()
    photo = models.ImageField(upload_to = 'media/main/feedbacks')
    date_added = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return self.name

class Contacts(models.Model):
    """For contacts page"""
    title = models.CharField(max_length=100)
    vk = models.URLField(max_length=150)
    email = models.EmailField(max_length=150)
    tlg = models.URLField(max_length=150)
    def __str__(self):
        return self.title

class Info (models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    def __str__(self):
        return self.title
