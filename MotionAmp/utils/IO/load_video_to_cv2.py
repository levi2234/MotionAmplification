import cv2

def load_video_to_cv2(video_path:str )->cv2.VideoCapture:
    """
    Load a video file into a cv2.VideoCapture object.

    Parameters:
    video_path (str): The path to the video file.

    Returns:
    cv2.VideoCapture: The cv2.VideoCapture object containing the video.
    """
    
    # Create a VideoCapture object
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return None
    
    
    
    return cap