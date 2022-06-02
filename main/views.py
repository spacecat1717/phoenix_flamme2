from django.shortcuts import render, redirect

from .models import Category, Item, Topic, Cart
from .forms import AddForm


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
    form = AddForm(request.POST, instance=item)
    #if request.method == 'POST':
    #    item = form.save()
    #    print('saved') #временная штука
     #   return redirect ('main:cart')  
    context = {'item': item, 'form':form}
    return render(request, 'main/item.html', context)

def show_cart(request):
    cart = Cart.objects.get(id=1)
    cart_items = cart.item_set.all()
    #if cart_item.small != "standart": хер знает где оставить
    #    cart_item.price -= 100
    context = {'cart_items': cart_items}
    return render(request, 'main/detail_cart.html', context)

def add_to_cart(request, item_id):
        item = Item.objects.get(id=item_id)
        form = AddForm(request.POST, instance=item)
        if request.method == 'POST':
            item = form.save()
            print('saved') #временная штука
            return redirect ('main:cart')
        return render(request, 'main/item.html')
        

   
    



