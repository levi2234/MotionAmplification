from MotionAmp.motion_amplification import eulerian_amplification

import time




video = eulerian_amplification('face_source.wmv', factor=[0,300,0], band=[0.4, 3], downsample_level=3)

