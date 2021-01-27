import cv2
import numpy as np
import os
import glob

img_array = []
files_to_proces = os.listdir(os.path.join("vid_detection"))
print(type(files_to_proces))
files_to_proces.sort()
print(files_to_proces)
for idx, filename in enumerate(files_to_proces): # enumerate(os.listdir(os.path.join("videos"))):
    print(filename)
    img = cv2.imread(os.path.join("vid_detection_dyn", str(filename)))

    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)
    img_array.append(img)
    img_array.append(img)

out = cv2.VideoWriter('cancer_2.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()