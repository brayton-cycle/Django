import requests

def hit(market):
    response = requests.get(f'https://public.coindcx.com/market_data/orderbook?pair={market}')
    return response