import os
import cv2
import numpy as np
from skimage.measure import structural_similarity as ssim


directory_path = "image_temp"


orb = cv2.ORB_create()
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

for root, dirs, files in os.walk(directory_path):
    _buffer = None
    for _file in files:
        if _buffer is not None:
            image = cv2.imread("/".join([directory_path,_file]))
            # do processing
            kp1, des1 = orb.detectAndCompute(_buffer,None)
            kp2, des2 = orb.detectAndCompute(image,None)
            # if des1 is not None and des2 is not None:
            matches = bf.match(des1,des2)
            print(np.mean([match.distance for match in matches])*len(matches))
            _bufer = image
        else:
            _buffer = cv2.imread("/".join([directory_path,_file]))