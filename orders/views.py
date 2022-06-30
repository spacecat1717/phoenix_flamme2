import time, datetime
from django.template import Template, Context
from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


NOTIFICATION_TEMPLATE = """
Новый заказ
Номер заказа : {{order.id}}
Дата: {{order.created}}
Клиент: {{order.first_name}} {{order.last_name}}
Адрес: {{order.postal_code}},{{order.city}}, {{order.address}}
Почта: {{order.email}}
Состав заказа:
{% for item in items %}
  Товар: {{item.product}} 
  Количество: {{item.quantity}} 
  Цена за штуку: {{item.price}}
  Цена за все: {{item.total_price}}
{% endfor %}
Комментарий: {{order.comment}}
Стоимость доставки: {{order.delivery_price}}
"""



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
            order_notification(order_id)
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
        'phoenix.flamme@mail.ru', 
        [email],
        fail_silently=False,
    )

def order_notification(order_id):
    #executing order info from db
    order = Order.objects.get(id=order_id)
    items = OrderItem.objects.filter(order=order)
    template = Template(NOTIFICATION_TEMPLATE)
    print(order, items)
    send_mail(
        'New order',
        template.render(context=Context({'order':order, 'items':items})),
        'phoenix.flamme@mail.ru',
        ['phoenix.flamme@mail.ru'],
        fail_silently=False,
    )
    



    
