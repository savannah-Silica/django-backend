from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

# Importing notification Consumer from consumers.py
from notification.consumers import NotificationConsumer

application = ProtocolTypeRouter({
    # Websocket chat handler
    'websocket': AllowedHostsOriginValidator(  # Only allow socket connections from the Allowed hosts in the settings.py file
        AuthMiddlewareStack(  # Session Authentication, required to use if we want to access the user details in the consumer
            URLRouter(
                [
                    # Url path for connecting to the websocket to send notifications.
                    path("notifications/", NotificationConsumer.as_asgi()),
                ]
            )
        ),
    ),
})
