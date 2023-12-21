# Import necessary modules for URL routing in Django.
from django.urls import re_path

# Import the 'VideoConsumer' class from the 'consumers' module of the current application.
from . import consumers

# Define WebSocket URL patterns for the application.

# Create a WebSocket URL pattern that captures the 'video_path' parameter from the URL.
# It routes WebSocket requests to the 'VideoConsumer' class using the 'as_asgi()' method.
websocket_urlpatterns = [
    re_path(r'ws/video/(?P<video_path>[\w\W]+)/$', consumers.VideoConsumer.as_asgi())
]
