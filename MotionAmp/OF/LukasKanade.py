#implement the lucas Kenade algorithm for optical flow

import numpy as np
import cv2
from MotionAmp.lib import progress
from matplotlib import pyplot as plt


#LUKASKANDAE OPTICAL FLOW 
"""
STILL DOES NOT WORK I think is with both the good features tracking and the need for LUKAS KANADE to 
recieve unsigned 8 bit arrays which is not the case for the numpy array of the video whcih has been converted to greyscale
The greyscale images are float 32 arrays with values between 0-1 which lose information when converted to unsigned 8 bit arrays

"""
def LukasKanade(video_array):
    # Extract shape of the input array
    width, height, num_frames = video_array.shape

    # Initialize arrays for phase, magnitude, and flow offsets

    flow_x = np.zeros((width, height, num_frames - 1))
    flow_y = np.zeros((width, height, num_frames - 1))

    # Parameters for Lucas-Kanade optical flow
    lk_params = dict(winSize=(15, 15), maxLevel=2, 
                     criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    for i in progress(range(num_frames - 1), "Calculating optical flow frame: "):
        # Get consecutive frames
        prev_frame = video_array[:, :, i]
        curr_frame = video_array[:, :, i + 1]
        
        
        # Convert frames to 8-bit
        prev_frame = cv2.convertScaleAbs(prev_frame) #this might be a problem because of information loss
        curr_frame = cv2.convertScaleAbs(curr_frame)

        
        # Find good features to track
        p0 = cv2.goodFeaturesToTrack(prev_frame, maxCorners=100, qualityLevel=0.001, minDistance=10, mask=None)
        
        if p0 is not None:
            # Calculate optical flow
            
            p1, st, err = cv2.calcOpticalFlowPyrLK(prev_frame, curr_frame, p0, None, **lk_params)

            # Select good points
            good_new = p1[st == 1]
            good_old = p0[st == 1]

            # Compute phase, magnitude, and flow offsets
            flow = good_new - good_old

            for (x, y),  flow_val in zip(good_new.astype(int),  flow):
    
                flow_x[y, x, i] = flow_val[0]
                flow_y[y, x, i] = flow_val[1]

    return flow_x, flow_y


