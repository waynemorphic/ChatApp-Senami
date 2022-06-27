from django.urls import re_path
from core import consumers

# we are calling as_asgi classmethod to get an ASGI application that instatiates an instance of our consumer
# for each user connection

# this is similar as as_view method in django

websocket_urlpatterns = [
    re_path(r'ws/Senami/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi())
]