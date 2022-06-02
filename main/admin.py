from django.contrib import admin
from .models import Category, Item, Topic, Cart

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Topic)
admin.site.register(Cart)

