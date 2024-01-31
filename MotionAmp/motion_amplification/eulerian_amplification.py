import logging
import numpy as np
from matplotlib import pyplot as plt
import os
import cv2

from MotionAmp.utils.IO import load_video_to_cv2
from MotionAmp.utils.IO import save_numpy_to_mp4
from MotionAmp.utils.convert import convert_video_to_numpy_array
from MotionAmp.data_processing.temporal_bandpass_filter import apply_temporal_bandpass_filter
from MotionAmp.data_processing.PyramidSampling import pyrDownsample
from MotionAmp.data_processing.PyramidSampling import pyrUpsample
from MotionAmp.data_processing.average_clipped_pixels import average_clipped_pixels

def eulerian_amplification(videopath:str,  band:list, factor:int =[0.1,0.1,0.1], downsample_level=2)->None:
    """
    Amplify motion in a video using Eulerian amplification technique.

    Args:
        videopath (str): Path to the video file.
        band (list): List of two values representing the lower and upper frequency band for the temporal bandpass filter.
        factor (list): List of three values representing the amplification factor for each color channel (blue, green, red).
        downsample_level (int): Level of pyramid downsampling.

    Returns:
        None
    """

    # Load the video into a NumPy array np.array([frame, height, width, channel])
    video = load_video_to_cv2(videopath)

    # Get the frame rate of the video
    framerate = video.get(cv2.CAP_PROP_FPS)

    # Convert the video to a NumPy array np.array([frame, height, width, channel])
    processed_video_array = convert_video_to_numpy_array(video)
    
    # Make a copy of the original video array
    original_video_array = processed_video_array.copy()

    # Downsample the video
    processed_video_array = pyrDownsample(processed_video_array, levels=downsample_level)

    # Extract the channels from the video
    blue_channel = processed_video_array[:, :, :, 2]  # Extract the blue channel from the video
    green_channel = processed_video_array[:, :, :, 1]  # Extract the green channel from the video
    red_channel = processed_video_array[:, :, :, 0]  # Extract the red channel from the video

    logging.warning("Extracted the channels from the video.")

    # Apply temporal bandpass filter to each channel separately
    blue_channel_filtered = apply_temporal_bandpass_filter(blue_channel, band[0], band[1], framerate)
    green_channel_filtered = apply_temporal_bandpass_filter(green_channel, band[0], band[1], framerate)
    red_channel_filtered = apply_temporal_bandpass_filter(red_channel, band[0], band[1], framerate)

    # Amplify the filtered channels
    blue_channel_amplified = blue_channel_filtered * factor[2]
    green_channel_amplified = green_channel_filtered * factor[1]
    red_channel_amplified = red_channel_filtered * factor[0]

    amplified_channels = np.stack((blue_channel_amplified, green_channel_amplified, red_channel_amplified), axis=3)

    # Check if a channel is clipped and if it is, replace the values in all channels with 0
    max_value = np.max(amplified_channels)
    min_value = np.min(amplified_channels)
    if max_value > 100 or min_value < 0:
        amplified_channels = np.where((amplified_channels > 100) | (amplified_channels < 0), 0, amplified_channels)
      

    

    
    # Upsample the video
    amplified_channels = pyrUpsample(amplified_channels, levels=downsample_level)

    # Add the amplified channels to the original video array
    original_video_array = original_video_array + amplified_channels

    # Normalize the video array to 0-255
    original_video_array = original_video_array / np.max(processed_video_array) * 255

    # Convert to integers for saving so that video is not clipped to 0-1 range because of float
    original_video_array = original_video_array.astype(np.uint8)
    
    # Save the amplified video
    workdir = os.getcwd()
    save_numpy_to_mp4(workdir + "/output.mp4", original_video_array, framerate)
    
    
    