# Import necessary modules for defining Django models.
from django.db import models

# Define a Django model named 'Video' for storing video files.

class Video(models.Model):
    # Define a 'video_file' field of type 'FileField' for uploading video files.
    # Uploaded videos will be stored in the 'videos/' directory.
    video_file = models.FileField(upload_to='videos/')
