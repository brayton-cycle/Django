from django.shortcuts import render

# Create your views here.
from apis.tasks import hit_url

# Call the Celery task asynchronously
result = hit_url('https://public.coindcx.com/market_data/orderbook?pair=B-BTC_USDT')

# Get the result from the task (blocking)
response_content = result.get()

print(response_content)