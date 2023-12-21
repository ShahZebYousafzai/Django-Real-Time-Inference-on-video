from django.contrib import admin
from django.urls import path
from . import views

# Define the URL patterns for the Django application.

urlpatterns = [
    # 1. Map the root URL (e.g., http://example.com/) to the 'uploadView' view function, with the name "index".
    path("", views.uploadView, name="index"),

    # 2. Map URLs with a format like "live_video/some_video_path" to the 'videoView' view function, with the name "live_video".
    # The <str:video_path> part captures the video_path as a string parameter.
    path("live_video/<str:video_path>", views.videoView, name="live_video"),
    path('get_timestamp/', views.get_timestamp, name='get_timestamp'),
]
