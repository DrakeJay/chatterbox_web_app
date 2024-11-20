

import os
from django.core.asgi import get_asgi_application
from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack

import chat.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messaging_app.settings')

print("ASGI application loaded successfully")

application =get_asgi_application({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})


