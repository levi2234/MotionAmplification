import cv2
import numpy as np
from MotionAmp.lib import progress

def convert_video_to_greyscale(video_array) -> np.ndarray:
    """
    Convert a video array to grayscale.

    Args:
        video_array (np.ndarray): The input video array with shape (height, width, num_frames, channels).

    Returns:
        np.ndarray: The grayscale video array with shape (height, width, num_frames).
    """
    # Get the shape of the original video
    height, width, num_frames, channels = video_array.shape

    # Initialize an array for the grayscale video with one channel
    grayscale_video = np.zeros((height, width, num_frames))
    

    for i in progress(range(num_frames), name="Converting to grayscale"):
        # Extract the frame
        frame = video_array[:, :, i, :]

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Store the grayscale frame
        grayscale_video[:, :, i] = gray_frame

    return grayscale_video