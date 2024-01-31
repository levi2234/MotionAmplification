# MotionAmplification

## Logs

### 2021-01-20
    The eulerian magnification is working, but the results are not great yet. The magnification is visible but the image is very noisy and not as smooth as the reference video from the original paper.

    I have started implementing the OF(optical flow in the lagrangian_amplification.py file. For now I chose to make use of the Lukas-Kanade method because it is claimed to work good with small motions which we aim for. 

    The problem Now is that converting the original RGB image to grayscale results in a float value for the brightness of each pixel. The built in Lukas-Kande method however requires a unisigned 8-bit integer as input. Converting the float values to uint8 results in a loss of information. This is where I stand now