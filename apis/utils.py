import requests
# from .credentials import secret,key # Check once
import datetime
import math
import hmac
import hashlib
import base64
import json
import time

def hit(market):
    response = requests.get(f'https://public.coindcx.com/market_data/orderbook?pair={market}')
    return response

def new_order(secret, side, market, price, quantity,client_order_id):
        secret_bytes = bytes(secret, encoding='utf-8')

        current_datetime = datetime.datetime.now()
        floored_timestamp = math.floor(current_datetime.timestamp())

        body = {
        "side": side,    #Toggle between 'buy' or 'sell'.
        "order_type": "limit_order", #Toggle between a 'market_order' or 'limit_order'.
        "market": market, #Replace 'SNTBTC' with your desired market pair.
        "price_per_unit": price, #This parameter is only required for a 'limit_order'
        "total_quantity": quantity, #Replace this with the quantity you want
        "timestamp": floored_timestamp,
        "client_order_id": client_order_id #Replace this with the client order id you want
        }

        json_body = json.dumps(body, separators = (',', ':'))

        signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

        url = "https://api.coindcx.com/exchange/v1/orders/create"

        headers = {
            'Content-Type': 'application/json',
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        }

        response = requests.post(url, data = json_body, headers = headers)
        data = response.json()
        print(data)

def cancel_all(secret, market):
    # python3
    secret_bytes = bytes(secret, encoding='utf-8')

    current_datetime = datetime.datetime.now()
    floored_timestamp = math.floor(current_datetime.timestamp())

    body = {
    "market": market, # Replace 'SNTBTC' with your desired market pair.
    "timestamp": floored_timestamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/orders/cancel_all"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)
