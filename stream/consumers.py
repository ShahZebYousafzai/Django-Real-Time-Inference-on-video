# Import the 'cv2' module, which is the OpenCV library for computer vision tasks.
import cv2

# Import the 'json' module for working with JSON data.
import json

# Import the 'asyncio' module for asynchronous programming support.
import asyncio

# Import the 'datetime' module for working with date and time.
import datetime

# Import the 'numpy' module for numerical and array operations.
import numpy as np

# Import a custom function 'serialize_frame' from the 'processing' module in the current application.
from .processing import serialize_frame

# Import the 'AsyncWebsocketConsumer' class from Django's 'channels.generic.websocket' module.
from channels.generic.websocket import AsyncWebsocketConsumer

# Define a custom WebSocket consumer class named VideoConsumer that handles WebSocket communication.
class VideoConsumer(AsyncWebsocketConsumer):
    # Define the 'connect' method for WebSocket connection handling.

    # This method is executed when a WebSocket connection is established.
    async def connect(self):
        # Accept the WebSocket connection.
        await self.accept()

        # Retrieve the video file path from the URL route parameters.
        video_file_path = self.scope['url_route']['kwargs']['video_path']

        # Send processed frames using the video file path.
        await self.send_processed_frames(video_file_path)

    # Define the 'send_frame' method for sending video frame data and match data to the WebSocket client.

    # This method takes 'frame_data' and 'match_data' as parameters and sends them as JSON to the WebSocket client.
    async def send_frame(self, frame_data, timestamp_str):
        # Convert the frame data and match data into a JSON format and send it to the client.
        await self.send(text_data=json.dumps({
            'frame_data': frame_data,
            'timestamp': timestamp_str
        }))

    # Define the 'send_processed_frames' method for processing and sending video frames and match data.
    # This method takes 'video_file_path' as a parameter and processes video frames and related data.
    async def send_processed_frames(self, video_file_path):
        # Initialize data structures and variables.
        # A dictionary for actions
        print(video_file_path)

        try:
            cap = cv2.VideoCapture(f"videos/{video_file_path}")

            # Start iterating over the frames
            while True:
                ret, frame = cap.read()

                if not ret:
                    break  # Break the loop if no more frames are available

                # Get the timestamp of the frame on which the prediction is being performed
                timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
                timestamp = datetime.timedelta(milliseconds=timestamp)

                timestamp_str = str(timestamp).split('.', 2)[0]

                # Encode the frames to base64 to send to the web
                frame_data = serialize_frame(frame)  # Implement the serialization function

                # Send the frame data and match data to the WebSocket client.
                await self.send_frame(frame_data, timestamp_str)
                # Adjust the frame rate as needed (e.g., 30 frames per second).
                await asyncio.sleep(0.033)

            # Release the video capture object outside the loop.
            cap.release()

        except Exception as e:
            # In case of an error, send an error message to the WebSocket client.
            await self.send(text_data=f"Error: {str(e)}")


    async def receive(self, text_data):

        # Handle messages from WebSocket
        message = json.loads(text_data)

        print(message)