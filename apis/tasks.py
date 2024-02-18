# yourapp/tasks.py

from celery import shared_task
import requests
from BOT.celery import app

@shared_task
def hit_url(url):
    response = requests.get(url)
    print("RESPONSE", response)
    return response.text

@app.task(name = 'sum two numbers')
def add(x,y):
    return x+y

@app.task(name = 'hit url')
def xyz():
    print('xuuadas')

# celery -A BOT worker -l info -f celery.logs