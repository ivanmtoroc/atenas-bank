# Channels
from channels.generic.websocket import AsyncWebsocketConsumer

# Tickets algorithm
from apps.tickets.algorithm import next_ticket

# JSON
import json

class TicketsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.tenant = self.scope['url_route']['kwargs']['tenant']
        await self.channel_layer.group_add(self.tenant, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.tenant, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        ticket = next_ticket(data['service'], data['tenant'])
        if ticket:
            ticket_data = {
                'ticket': {
                    'id': ticket.id,
                    'turn_number': ticket.turn_number,
                    'user': ticket.user
                },
                'status': True,
                'operator': data['operator']
            }
        else:
            ticket_data = {
                'ticket': {},
                'status': False,
                'operator': data['operator']
            }

        await self.channel_layer.group_send(
            self.tenant,
            { 'type': 'next_ticket', 'ticket': ticket_data }
        )

    async def next_ticket(self, context):
        await self.send(text_data = json.dumps(context['ticket']))
