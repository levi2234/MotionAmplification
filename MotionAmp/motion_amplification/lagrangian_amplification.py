import cv2
import numpy as np
import matplotlib.pyplot as plt
from MotionAmp.OF import LukasKanade
import os 

from MotionAmp.utils.IO import load_video_to_cv2
from MotionAmp.utils.IO import save_numpy_to_mp4
from MotionAmp.utils.convert import convert_video_to_greyscale
from MotionAmp.utils.convert import convert_video_to_numpy_array


def lagrangian_amplification(videopath:str)->None:
    

    # Load the video into a NumPy array np.array([frame, height, width, channel])
    video = load_video_to_cv2(videopath) #cv2 video object
    
    #framerate
    framerate = video.get(cv2.CAP_PROP_FPS) #get frame rate of video
    
    #convert to numpy array
    video = np.float32(convert_video_to_numpy_array(video)) /255.0 #normalize to 0-1

    if len(video.shape) == 4:
        video = np.float32(convert_video_to_greyscale(video)) /255.0 #normalize to 0-1
        
    x_flow,y_flow = LukasKanade(video)
    mag = np.sqrt(x_flow**2 + y_flow**2)
    print(max(mag.flatten()))
    
    print(x_flow[5])


    
    
    

    
    
    
    
