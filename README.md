# MotionAmplification

This is a Python implementation of the Motion Amplification algorithm. The algorithm is based on the paper "Eulerian Video Magnification for Revealing Subtle Changes in the World" by MIT researchers Hao-Yu Wu, Michael Rubinstein, Eugene Shih, John Guttag, Frédo Durand, and William T. Freeman. The paper can be found [here](http://people.csail.mit.edu/mrub/*paprs*/vidmag.pdf).

The algorithm works by amplifying the motion in a video. It does this by first decomposing the video into its spatial and temporal components using a Laplacian pyramid. The temporal component is then amplified by a user-defined factor and added back to the spatial component. The resulting video is then reconstructed from the amplified spatial component.




# How to use the code
``` python
from MotionAmp.motion_amplification import eulerian_amplification
from MotionAmp.motion_amplification import lagrangian_amplification
import time

factor = [0, 70, 0] #amplication factor per color channel
band = [0.4, 3] #bandpass filter what frequencies to amplify
downsample_level = 3 #downsample the video to speed up the process and eliuminate high frequency noise

video = eulerian_amplification('face_source.wmv', factor=factor, band=band, downsample_level=downsample_level)

#result is stored under output.mp4 in the current directory
```


# Technical details

* **Step1**: The paper first decomposes the video into its spatial and temporal components using a Laplacian pyramid. Here however we use the Gaussian pyramid to decompose the video into a lower resolution version of the video.It applies a Gaussian filter to the input image to reduce high-frequency noise. This is achieved using a convolution operation with a Gaussian kernel. After smoothing, the image is downsampled by keeping only every alternate pixel in both rows and columns. This reduces the resolution of the image by a factor of 2. This process is repeated to obtain a series of images of decreasing resolution. The resulting images are called the Gaussian pyramid.

* ![image](https://github.com/levi2234/MotionAmplification/assets/10477282/f8444ef1-afb2-4bea-8b17-e182c9477950)


