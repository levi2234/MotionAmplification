import cv2
import numpy as np
import matplotlib.pyplot as plt
def convert_video_to_numpy_array(video) -> np.ndarray:
    """
    Load a video file and convert it into a NumPy array of frames.

    Parameters:
    video_path (str): The path to the video file.

    Returns:
    np.ndarray: The NumPy array containing the frames of the video. The shape of the array is np.array([num_frames, height, width, channels]).
    """
    
    # Create a VideoCapture object
    cap = video

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return None

    frames = []

    # Read the video frame by frame
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Append each frame to the frames list
        
        #convert frame to rgb
        
        frames.append(frame)

    # Release the VideoCapture object
    cap.release()

    # Convert the list of frames to a NumPy array
    frames_array = np.array(frames)

    #set the type of the array to float32
    frames_array = frames_array.astype(np.float32)
    

    return frames_array
