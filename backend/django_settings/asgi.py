import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django_app import urls_a

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_settings.settings')

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(URLRouter(urls_a.websocket_urlpatterns)),
    }
)