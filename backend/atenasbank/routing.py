# Channels
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

# Routings
from apps.tickets import routing as tickets_routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            tickets_routing.websocket_urlpatterns
        )
    ),
})
