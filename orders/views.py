from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    """create order with user's data"""
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            email = order.email
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         total_price=(item['price']*item['quantity']))
            # очистка корзины
            cart.clear()
            delivery = order.delivery_price
            order_mail(email)
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

def order_mail(email):
    send_mail (
        'Заказ принят',
        'Спасибо за ваш заказ в магазине Phoenix Flamme. \n Сразу после отправки мы пришлем вам трек-номер :)\nХорощего дня!',
        'lea.candlespace@gmail.com', #need to make normal email!!!
        [email],
        fail_silently=False,
    )