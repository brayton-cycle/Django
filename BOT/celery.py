import os
from celery import Celery 
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BOT.settings")
BASE_REDIS_URL = os.environ.get('REDIS_URL', "redis://localhost:6379") #this can be a separate worker server
app = Celery("BOT_celery")
app.config_from_object("django.conf:settings", namespace = 'CELERY') 
app.conf.result_backend = 'redis://localhost:6379/0'
app.autodiscover_tasks()
app.conf.broker_url = BASE_REDIS_URL
app.conf.beat_schedule = {
    'hit-url-every-10-seconds': {
        'task': 'apis.tasks.hit_url',  # Adjust the task name
        'schedule': 10.0,  # Interval in seconds
        'args': ('https://public.coindcx.com/market_data/orderbook?pair=B-BTC_USDT',),
    },
}
app.conf.beat_scheduler = 'celery.beat.PersistentScheduler'
app.autodiscover_tasks()