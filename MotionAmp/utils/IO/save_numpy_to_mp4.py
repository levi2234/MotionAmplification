import cv2
import numpy as np

def save_numpy_to_mp4(output_path, frames, fps):
    """
    Save a NumPy array of frames as a video file.

    Parameters:
    frames (np.ndarray): The NumPy array containing the frames of the video. The shape of the array is np.array([num_frames, height, width, channels]).
    fps (float): The frames per second of the video.
    output_path (str): The path to save the video file to.
    """
    
    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    height, width = frames.shape[1], frames.shape[2]
    video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Write the frames to the video file
    for frame in frames:
        
        video.write(frame)

    # Release the VideoWriter
    video.release()