# MotionAmplification

This is a Python implementation of the Motion Amplification algorithm. The algorithm is based on the paper "Eulerian Video Magnification for Revealing Subtle Changes in the World" by MIT researchers Hao-Yu Wu, Michael Rubinstein, Eugene Shih, John Guttag, Frédo Durand, and William T. Freeman. The paper can be found [here](http://people.csail.mit.edu/mrub/*paprs*/vidmag.pdf).

The algorithm works by amplifying the motion in a video. It does this by first decomposing the video into its spatial and temporal components using a Laplacian pyramid. The temporal component is then amplified by a user-defined factor and added back to the spatial component. The resulting video is then reconstructed from the amplified spatial component.

#comparing the original and amplified video
![Original](output.webm) ![Amplified](output.webm)
