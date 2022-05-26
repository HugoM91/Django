from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'^ws/socket-server/market_orders', consumers.MrkOrderConsumer.as_asgi())
]
