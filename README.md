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

  ![image](https://github.com/levi2234/MotionAmplification/assets/10477282/f8444ef1-afb2-4bea-8b17-e182c9477950)

* **Step2**: Now we have a low resolution version of the video. We can now amplify the motion in the video. This process is done on a pixel by pixel basis where we deconstruct the change in pixels over time using a Fast-Fourier-Transform. Using this transform we can isolate the frequency of the motion in the video and isolate a certain bandpass of frequencies to hone in on the desired frequencies. 

* **Step3**: After Isolating the fequencies within the Fast-Fourier Transform we amplify the bandpass-frequencies and reconstruct the video using the inverse Fast-Fourier-Transform. In the example above we amplify the frequencies by a factor of 70 and focus on a bandpass of 0.4 to 3 Hz, isolating the heart rate of the person in the video. 
  ![image](
https://docs.google.com/drawings/d/e/2PACX-1vTNvKWBeySLGVPifC-4rk22gs7XgSD7p1iqEg6eIPKtl3v9IWWgdCEv41P-iIJ70BZnlS6xjByCZafT/pub?w=1440&h=810)

* **Step4**: Now that we are left with a video with amplified motion we can reconstruct the video using the inverse Gaussian pyramid. This is done by upsampling the video and adding the amplified motion to the original video. This process is repeated until we have the original resolution of the video. Because we lose some information when downsampling the video we will have to interpolate the video to fill in the missing information. Or in our case we can just use the original video to fill in the missing information by overplotting the reconstructed video on top of the original video.
