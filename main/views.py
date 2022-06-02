from django.shortcuts import render, redirect

from .models import Category, Item, Topic
from cart.forms import CartAddProductForm


def index (request):
    """main page"""
    return render(request, 'main/index.html')

def categories(request):
    """list of caregories"""
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'main/categories.html', context)

def category(request, category_id):
    """one category with items list"""
    category = Category.objects.get(id=category_id)
    items = category.item_set.order_by('title')
    context = {'items': items}
    return render (request, 'main/category.html', context)
    
def topics(request):
    """list of topics"""
    topics = Topic.objects.order_by('title')
    context = {'topics':topics}
    return render(request, 'main/topics.html', context)

def item(request, item_id):
    """one item page"""
    item = Item.objects.get(id=item_id)  
    cart_product_form = CartAddProductForm()    
    context = {'item': item, 'cart_product_form': cart_product_form}
    return render(request, 'main/item.html', context)






        

   
    



