"""
WSGI config for flamme project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os, time, datetime

from django.core.wsgi import get_wsgi_application
from django.core.mail import BadHeaderError, send_mail
from orders.models import Order

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flamme.settings')
application = get_wsgi_application()

from orders.tasks import send_track
send_track.delay()
print('it runs') #test
