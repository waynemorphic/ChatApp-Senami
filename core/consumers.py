import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

### enabling channel layer

# here we are developing a synchronous WebSocket consumer that accepts all connections,
# receives messages from its client and echos those messages back to the same client

# note that any channel supporting asynchronous consumers should avoid to perform blocking
# operations such as accessing a django model.

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.scope obtains the room name from the url route in chat routing that opened the websocket connection
        # to the consumer
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        
        # the line below constructs a channel group name directly from the user specified room name without quoting or escaping
        self.room_group_name = 'chat_%s' % self.room_name
        
        # join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        # the line below accepts the websocket connection. If not called, the connection will be rejected and closed
        # rejection can be preferred if the requesting user is not authorized to perform the requested action
        await self.accept()
        
    async def disconnect(self, close_code):
        # leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        
        # send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )
        
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        
        await self.send(text_data = json.dumps({
            "message": message,
            "username": username
        }))