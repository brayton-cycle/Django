# myapp/consumers.py

import json
import time
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import requests
from .utils import hit


class TradeConsumer(AsyncWebsocketConsumer):

    async def receive(self, text_data):
        pass

    async def send_trade_data(self, event):
        trade_data = event['trade_data']

    async def connect(self):
        await self.accept()
        self.is_running = True
        while self.is_running:
            # await asyncio.sleep(2)  # Wait for 2 seconds
            # Hit the URL to check for condition
            buy_market = "B-XAI_USDT"
            trade_market = "B-USDT_INR"
            sell_market = "B-XAI_INR"

            trade_response = hit(trade_market)
            buy_response = hit(buy_market)
            sell_response = hit(sell_market)

            trade = json.loads(trade_response.content.decode('utf-8'))
            buy = json.loads(buy_response.content.decode('utf-8'))
            sell = json.loads(sell_response.content.decode('utf-8'))

            bids = trade.get("bids", {})
            max_bid = max(bids, key=lambda k: float(bids[k]))
            one_rupee_dollars = 1/float(max_bid)
            print( f" 1 rupee will give {one_rupee_dollars} dollars")

            bids = buy.get("bids", {})
            max_bid_sol = max(bids, key=lambda k: float(bids[k]))
            dollars_sol = 1/float(max_bid_sol)
            one_rupee_dollars_sol = dollars_sol*one_rupee_dollars
            print( f" And these many dollars will give {one_rupee_dollars_sol} SOLs")

            asks = sell.get("asks", {})
            min_ask = min(asks, key=lambda k: float(asks[k]))
            one_rupee_sol = 1/float(min_ask)
            print( f" And one rupee will give {one_rupee_sol} SOLs")

            sol_diff = one_rupee_dollars_sol-one_rupee_sol
            if sol_diff>0:
                print("profit :", sol_diff)
            else:
                print("loss :", sol_diff)

            print("\n")
            # print(str(buy_response),"\n\n")
            # print(str(sell_response))
            # await self.send(text_data=json.dumps(sell_response))
            await asyncio.sleep(2)

    async def disconnect(self, close_code):
        self.is_running = False
            
            # data = response.json()
            # if data.get('a', False):
            #     # Make trade using API/view
            #     response = requests.post('http://example.com/make_trade/')
            #     trade_data = response.json()
            #     # Send trade data to WebSocket client
            #     await self.send(text_data=json.dumps({
            #         'trade_data': trade_data
            #     }))

# myapp/consumers.py





