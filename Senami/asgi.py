"""
ASGI config for Senami project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import core.routing
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Senami.settings')

django_asgi_app = get_asgi_application()

# when a connection is made to the channels server, the ProtocolTypeRouter firsts inspects the of connection

# if connection is websocket type, the connection will be given to the AuthMiddlewareStack

# AuthMiddlewareStack populates the connection scope with reference to the currently authenticated user.
# this works similar to the request in django for an authenticated user
application = ProtocolTypeRouter({
    "http": django_asgi_app ,
    "websocket": AllowedHostsOriginValidator(
    AuthMiddlewareStack(
        URLRouter(
            core.routing.websocket_urlpatterns)
    ),
    )
    }) 
