# Channesl
from channels.generic.websocket import AsyncWebsocketConsumer

# Python
import json

# Algorithm
from . import algorithm

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
        data = json.loads(text_data)
        ticket = algorithm.next_ticket(data['service'])
        if ticket:
            ticket_data = {
                'ticket': {
                    'id': ticket.id,
                    'turn_number': ticket.turn_number,
                    'user': ticket.user
                },
                'with-ticket': True,
                'operator': data['operator']
            }
        else:
            ticket_data = {
                'with-ticket': False,
                'operator': data['operator']
            }

        await self.channel_layer.group_send(
            'tickets',
            {
                'type': 'next_ticket',
                'ticket': ticket_data
            }
        )

    async def next_ticket(self, context):
        await self.send(text_data = json.dumps(
            context['ticket']
        ))
