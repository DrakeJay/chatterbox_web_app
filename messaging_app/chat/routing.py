from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('chatroom/', consumers.ChatConsumer.as_asgi()),
]