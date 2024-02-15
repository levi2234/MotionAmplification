# MotionAmplification

This is a Python implementation of the Motion Amplification algorithm. The algorithm is based on the paper "Eulerian Video Magnification for Revealing Subtle Changes in the World" by MIT researchers Hao-Yu Wu, Michael Rubinstein, Eugene Shih, John Guttag, Frédo Durand, and William T. Freeman. The paper can be found [here](http://people.csail.mit.edu/mrub/*paprs*/vidmag.pdf).

The algorithm works by amplifying the motion in a video. It does this by first decomposing the video into its spatial and temporal components using a Laplacian pyramid. The temporal component is then amplified by a user-defined factor and added back to the spatial component. The resulting video is then reconstructed from the amplified spatial component.

My result
[output.webm](https://github.com/levi2234/MotionAmplification/assets/10477282/be585823-e686-4852-99ee-2f2abe0131f4)
Paper Result
[face_result.webm](https://github.com/levi2234/MotionAmplification/assets/10477282/c1bc3f53-1228-4c1f-99d9-285952b6b47b)
