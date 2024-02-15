# MotionAmplification

This is a Python implementation of the Motion Amplification algorithm. The algorithm is based on the paper "Eulerian Video Magnification for Revealing Subtle Changes in the World" by MIT researchers Hao-Yu Wu, Michael Rubinstein, Eugene Shih, John Guttag, Frédo Durand, and William T. Freeman. The paper can be found [here](http://people.csail.mit.edu/mrub/*paprs*/vidmag.pdf).

The algorithm works by amplifying the motion in a video. It does this by first decomposing the video into its spatial and temporal components using a Laplacian pyramid. The temporal component is then amplified by a user-defined factor and added back to the spatial component. The resulting video is then reconstructed from the amplified spatial component.

#comparing the original and amplified video

[face_result.webm](https://github.com/levi2234/MotionAmplification/assets/10477282/8e8be1b0-8e50-4046-b3a5-a5fed7c7ce48)
[output.webm](https://github.com/levi2234/MotionAmplification/assets/10477282/c63b0ae3-4f03-4cab-9401-65a63a25cdc1)
