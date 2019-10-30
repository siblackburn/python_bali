import sys
import os
import cv2
import numpy as np
import glob
 
 
path_prefix = sys.argv[1]
print(path_prefix)

img_array = []
for filename in sorted(glob.glob(f'{path_prefix}*.jpg'), key=os.path.basename):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter('out.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 30, size)
print(f'video: out.mp4')
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()