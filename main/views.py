from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Item, Topic


def index (request):
    return render(request, 'main/index.html')

def categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'main/categories.html', context)

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    items = category.item_set.order_by('title')
    context = {'items': items}
    return render (request, 'main/category.html', context)
    
def topics(request):
    topics = Topic.objects.order_by('title')
    context = {'topics':topics}
    return render(request, 'main/topics.html', context)

def item(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {'item': item}
    return render(request, 'main/item.html', context)

def change_quantity(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {'item': item}
    if request.method == 'GET':
        item.quantity +=1
        item.save()
    return render(request, 'main/item.html', context)

        

   
    



