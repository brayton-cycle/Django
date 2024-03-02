# project/urls.py

from django.urls import path
from django.urls import include
from apis import routing
urlpatterns = [
    path('', include(routing.websocket_urlpatterns)),
]

# project/urls.py