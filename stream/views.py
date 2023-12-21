# Import necessary modules and components from Django and the current application.

# Import the 'render' and 'redirect' functions from Django's 'shortcuts' module.
from django.shortcuts import render, redirect
from django.http import JsonResponse

# Import the 'VideoUploadForm' class from the current application's 'forms' module.
from .forms import VideoUploadForm

# Import the 'VideoConsumer' class from the current application's 'consumers' module.
from .consumers import VideoConsumer

# Import the 'os' module for operating system-related functionality.
from os.path import basename


# Define a function named windows_to_linux_path that converts a Windows file path to a Linux file path.
def windows_to_linux_path(windows_path):
    # Replace backslashes in the Windows path with forward slashes to make it compatible with Linux.
    linux_path = windows_path.replace('\\', '/')
    
    # Return the converted Linux path.
    return linux_path


# Define a view function named uploadView that handles video file uploads.

def uploadView(request):
    # Create an instance of the VideoUploadForm to handle video file uploads.
    form = VideoUploadForm()

    # Check if the request method is POST, indicating a form submission.
    if request.method == 'POST':
        # Create a VideoUploadForm instance with the POST data and uploaded files.
        form = VideoUploadForm(request.POST, request.FILES)
        
        # Check if the form data is valid.
        if form.is_valid():
            # If the form is valid, save the uploaded video and get the corresponding model instance.
            video = form.save()
            
            # Redirect to a 'live_video' view while passing the video file path as a parameter.
            # This is commonly used to display or stream the uploaded video.
            return redirect('live_video', video_path=basename(video.video_file.path))
    
    # Render the 'upload.html' template with the form, whether it's a GET request or a POST request with invalid data.
    return render(request, 'stream/upload.html', {'form': form})


# Define a view function named videoView that displays a video using a WebSocket consumer.

def videoView(request, video_path):
    # Convert the provided video_path to a Linux-style path using the windows_to_linux_path function.
    # video_path = fr'{windows_to_linux_path(os.path.relpath(video_path))}'
    
    # Create an instance of the WebSocket consumer to handle WebSocket communication.
    consumer = VideoConsumer()

    # Send the processed frames (video_path) to the WebSocket consumer.
    consumer.send_processed_frames((video_path))

    # Define the context dictionary with the 'video_path' variable for use in the template.
    context = {
        'video_path': video_path,
    }
    
    # Render the 'view.html' template and pass the context data to the template for rendering.
    return render(request, 'stream/view.html', context=context)

def get_timestamp(request):
    return JsonResponse("We are going to get the timestamp", safe=False)