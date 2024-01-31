import cv2
import numpy as np
from MotionAmp.lib import progress
def pyrDownsample(video, levels=2):
    """
    Downsample the video using Gaussian pyramid
    Parameters
    ----------
    video : np.array
        The video to be downsampled
    levels : int
        The number of levels in the Gaussian pyramid
    Returns
    -------
    video : np.array
        The downsampled video
    """
    print(type(video), np.shape(video))

    #iterate over frames
    N_frames = video.shape[0]
    newvideo = video
    print("downsampling video", levels, "times")
    
    for _ in progress(range(levels), name="Downsampling video steps"):
        #check if dimensions are even
        if newvideo.shape[1] % 2 != 0 or newvideo.shape[2] % 2 != 0:
            print("dimensions are not even")
            return newvideo
       
        newframes = []
        for i in range(N_frames):
        #iterate over levels
            newframes.append(cv2.pyrDown(newvideo[i,:,:,:]))
        newvideo = np.array(newframes) 

    return np.array(newvideo)



def pyrUpsample(video, levels=2):
    """
    Upsample the video using Gaussian pyramid
    Parameters
    ----------
    video : np.array
        The video to be upsampled
    levels : int
        The number of levels in the Gaussian pyramid
    Returns
    -------
    video : np.array
        The upsampled video
    """
    #iterate over frames
    N_frames = video.shape[0]
    newvideo = video
    print("upsampling video", levels, "times")
    for _ in progress(range(levels), name="Upsampling video steps"):
        
        
        new_frames = []
        for i in range(N_frames):
        #iterate over levels
            new_frames.append(cv2.pyrUp(newvideo[i,:,:,:]))
        newvideo = np.array(new_frames)
    return np.array(newvideo)
            