from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Cart, CartItem
from main.forms import CartItemCreateForm

class DetailCart(ListView):
    model = Cart
    template_name = 'cart/detail_cart.html'
    #def get_context_data(self, **kwargs):
    #    context = super(DetailCart, self).get_context_data(**kwargs)
    #    context['cart_items'] = CartItem.objects.all()
    #    return context



#class DeleteCart(DeleteView):
#   model = Cart
#    template = 'cart/delete_cart.html'

"""CartItem views"""

class CartItemCreate(CreateView):
    template_name = 'main/category.html'
    form_class = CartItemCreateForm

class DeleteCartItem(DeleteView):
    model = Cart
    template_name = 'cartitem/delete_cartitem.html'