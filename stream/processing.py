import cv2
import base64
import numpy as np

def serialize_frame(frame):
    # Ensure the frame is a NumPy array with uint8 data type
    if isinstance(frame, np.ndarray) and frame.dtype == np.uint8:
        # Encode the frame data as Base64
        frame_data = cv2.imencode('.jpg', frame)[1].tobytes()
        frame_data = base64.b64encode(frame_data).decode('utf-8')
        return frame_data
    else:
        raise ValueError("Invalid frame format")

def deserialize_frame(frame_data):
    # Decode the Base64 data and convert it back to a NumPy array
    frame_bytes = base64.b64decode(frame_data)
    frame = np.frombuffer(frame_bytes, dtype=np.uint8)
    return frame
