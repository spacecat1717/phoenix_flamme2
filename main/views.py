from django.shortcuts import render, redirect

from django.core.files.storage import FileSystemStorage
from .models import Category, Item, Topic, Feedback
from cart.forms import CartAddProductForm
from .forms import FeedbackForm

"""Basic views"""

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

"""Feedback views"""

def add_feedback(request):
    """new feedback"""
    form = FeedbackForm()
    if request.method != 'POST':
        form = FeedbackForm()
    elif request.method == 'POST':
        photo = request.FILES['feedback']
        fs = FileSystemStorage()
        filename = fs.save(photo, photo)
        file_url = fs.url(filename)
        form = FeedbackForm(request.POST)
        if form.is_valid():
         new_feedback = form.save()
         return redirect('main:feedback_list')
    context = {'form': form}
    return render (request, 'main/new_feedback.html', context)

def feedback_list(request):
    """list of feedbacks"""
    feedbacks = Feedback.objects.order_by('-date_added')
    context = {'feedbacks': feedbacks}
    return render (request, 'main/feedbacks.html', context)









        

   
    



