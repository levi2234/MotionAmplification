import numpy as np

def average_clipped_pixels(video_array, max=255):
    
    #remove all values above max and replace by average of surrounding pixels
    
    for i in range(video_array.shape[0]):
        for color in range(video_array.shape[3]):
            frame = video_array[i,:,:,color]
            
            #find index of pixels above max
            idx = np.where(frame >= max)
            
            #replace those pixels with average of surrounding pixels
            for j in range(len(idx[0])):
                #find average of surrounding pixels
                avg = np.mean(frame[idx[0][j]-1:idx[0][j]+2, idx[1][j]-1:idx[1][j]+2])
                #replace pixel with average
                frame[idx[0][j], idx[1][j]] = avg
            
            video_array[i,:,:,color] = frame
    return video_array
        

    