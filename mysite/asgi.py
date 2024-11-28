import os

from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

import app.routing
import chat.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
                app.routing.websocket_urlpatterns +
                chat.routing.websocket_urlpatterns,
            )
    ),
})
