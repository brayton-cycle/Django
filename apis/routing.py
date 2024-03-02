# myapp/routing.py

from django.urls import path
from .consumers import TradeConsumer

websocket_urlpatterns = [
    path('ws/', TradeConsumer.as_asgi()),
]
