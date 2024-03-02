from django.shortcuts import render
import hmac
import hashlib
import base64
import json
import time
import requests
from rest_framework.views import APIView
from .credentials import secret,key
import datetime
import math


def print_hit_url():
    # Create your views here.
    from apis.tasks import hit_url

    # Call the Celery task asynchronously
    result = hit_url('https://public.coindcx.com/market_data/orderbook?pair=B-BTC_USDT')

    # Get the result from the task (blocking)
    response_content = result.get()

    print(response_content)

class NewOrder(APIView):
    def post(self, request, *args, **kwargs):
        pass
        # python3








