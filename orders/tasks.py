import datetime
from django.core.mail import BadHeaderError, send_mail
from .models import Order
from flamme.celery import app

"""For sending tracks"""

@app.task
def send_track():
    """executing emails from orders(last week) and send tracks to customers"""
    #executed orders from sat to fri (6 days)
    #execution begins every sat at 0:00
    #FINAL
    start = datetime.datetime.now() - datetime.timedelta(days=1)
    period = start - datetime.timedelta(days=3)
    #TEST
    #start = datetime.datetime.now()
    #period = start - datetime.timedelta(hours=3)
    orders = Order.objects.filter(created__range=(period, start))
    for order in orders:
        if order.track:
            track = order.track
            email = order.email
            send_track_test(track, email)

def send_track_test(track, email):
    track = str(track)        
    send_mail('Phoenix Flamme', 
        'Ваш заказ отправлен\nНомер для отслеживания '+track,
        'phoenix.flamme@mail.ru', 
        [email]) 