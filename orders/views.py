import time, datetime
#from datetime import timedelta, date
from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from .models import OrderItem, Order
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
            order_id = order.id
            order_mail(email, order_id)
            execute_data()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

def order_mail(email, order_id):
    """sending email to customer after order"""
    order_id = str(order_id)
    send_mail (
        'Phoenix Flamme',
        'Спасибо за ваш заказ в магазине Phoenix Flamme. \nСразу после отправки мы пришлем вам трек-номер :)\nНомер вашего заказа: '+order_id,
        'phoenix.flamme@mail.ru', #need to make normal email!!!
        [email],
        fail_silently=False,
    )

"""For sending tracks"""

def execute_data():
    """executing emails from orders(last week)"""
    now = datetime.datetime.now()
    week = now-datetime.timedelta(days=1)
    orders = Order.objects.filter(created__range=(week, now))
    for order in orders:
        if order.track:
            track = order.track
            email = order.email
            send_track(track, email)  
            

def send_track(track, email):
    """send email with track to customer"""
    track = str(track)
    send_mail('Phoenix Flamme', 
            'Ваш заказ отправлен\nНомер для отслеживания '+track,
             'phoenix.flamme@mail.ru', 
             [email])

    
