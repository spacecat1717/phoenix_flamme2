import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flamme.settings')

app = Celery('flamme')
app.config_from_object('django.conf:settings')
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

#TEST
app.conf.beat_schedule = {
                'check-db-every-single-minute': {
                'task': 'orders.tasks.send_track',
                'schedule': crontab(),
    },
}

#FINAL!!!!!
#app.conf.beat_schedule = {
    
    #'run every saturday at midnight': {'task': 'orders.tasks.send_track',
    #        'schedule': crontab(minute='0', hour='0', day_of_week='sat') },
    #                    }