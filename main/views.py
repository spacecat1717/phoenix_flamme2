import random
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.core.files.storage import FileSystemStorage
from .models import Category, Item, Topic, Feedback, Contacts, Info
from cart.forms import CartAddProductForm
from .forms import FeedbackForm

"""Basic views"""

def index (request):
    """main page"""
    #on main page will show items that have 'show_on_main' field
    items = Item.objects.filter(show_on_main=True)    
    return render(request, 'main/index.html', {'items':items})

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

def item(request, item_id):
    """one item page"""
    item = Item.objects.get(id=item_id)  
    cart_product_form = CartAddProductForm()   
    context = {'item': item, 'cart_product_form': cart_product_form}
    return render(request, 'main/item.html', context)

"""Topics views"""

def topics(request):
    """list of topics"""
    topics = Topic.objects.order_by('title')
    context = {'topics':topics}
    return render(request, 'main/topics.html', context)

def topic(request, topic_id):
    """one topic"""
    topic = Topic.objects.get(id=topic_id)
    context = {'topic': topic}
    return render(request, 'main/topic.html', context)


"""Feedback views"""

def add_feedback(request):
    """new feedback"""
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return  redirect('main:feedback_list')
        else:    
            form = FeedbackForm()
    return render (request, 'main/new_feedback.html', {'form': form})


def feedback_list(request):
    """list of feedbacks"""
    feedbacks = Feedback.objects.order_by('-date_added')
    context = {'feedbacks': feedbacks}
    return render (request, 'main/feedbacks.html', context)

"""contacts view"""

def contacts(request):
    contacts = Contacts.objects.all()
    context = {'contacts': contacts}
    return render (request, 'main/contacts.html', context)

def info(request):
    parts = Info.objects.all()
    context = {'parts': parts}
    return render (request, 'main/info.html', context)









        

   
    



