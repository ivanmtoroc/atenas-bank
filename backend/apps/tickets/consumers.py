# Channesl
from channels.generic.websocket import AsyncWebsocketConsumer

# Python
import json

class TicketsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'tickets',
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'tickets',
            self.channel_name
        )

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            'tickets',
            {
                'type': 'next_ticket',
                'ticket': 'G04'
            }
        )

    async def next_ticket(self, event):
        ticket = event['ticket']

        await self.send(text_data = json.dumps({
            'ticket': ticket
        }))
