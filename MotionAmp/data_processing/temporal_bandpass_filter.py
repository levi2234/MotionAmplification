from numpy.fft import fft, ifft
import numpy as np 


def apply_temporal_bandpass_filter(frames, low_freq, high_freq, fps):
    """
    Applies a temporal filter to the input frames. Only allow for a single channel

    Args:
        frames (list): List of frames to be filtered.
        low_freq (float): Lower frequency cutoff for the bandpass filter.
        high_freq (float): Higher frequency cutoff for the bandpass filter.
        fps (float): Frames per second of the input frames.

    Returns:
        numpy.ndarray: Filtered frames in the time domain.
    """
    
    # Convert frames to numpy array
    frames_array = np.array(frames)
    
    # Apply FFT on each pixel throughout the frames
    freq_repr = fft(frames_array, axis=0)

    # Create a bandpass filter
    frequencies = np.fft.fftfreq(frames_array.shape[0], d=1.0/fps)
    bound_low = (np.abs(frequencies - low_freq)).argmin()
    bound_high = (np.abs(frequencies - high_freq)).argmin()
    filter_mask = (frequencies > low_freq) & (frequencies < high_freq)

    # Apply filter in frequency domain
    freq_repr[~filter_mask] = 0

    # Apply inverse FFT to convert back to time domain
    filtered_frames = ifft(freq_repr, axis=0).real
    
    #convert the filtered frames to same type as input frames
    filtered_frames = filtered_frames.astype(frames_array.dtype)

    return filtered_frames