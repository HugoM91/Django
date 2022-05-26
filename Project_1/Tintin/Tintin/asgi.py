"""
ASGI config for Tintin project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import market_orders.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tintin.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            market_orders.routing.websocket_urlpatterns
        )
    )
})
