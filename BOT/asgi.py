import os
from .wsgi import *
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import apis.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BOT.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            apis.routing.websocket_urlpatterns
        )
    )
    # Just HTTP for now. (We can add other protocols later.)
})