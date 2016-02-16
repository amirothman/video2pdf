import copy
import cv2
from scipy import spatial
import numpy as np

sourceVideo = "Sutherland-Hodgman_Polygon_Clipping_Algorithm-S091lKYWbSs.mp4"
cam = cv2.VideoCapture(sourceVideo)

_count = 0
_buffer = None

orb = cv2.ORB_create()
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
arr = []
arr_frame = []
while True:
    ret, img = cam.read()                      
    if (type(img) == type(None)):
        break
    if (0xFF & cv2.waitKey(5) == 27) or img.size == 0:
        break
    #print(count)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if _buffer is not None:
        if _count % 30 == 0:
            #kp1, des1 = orb.detectAndCompute(_buffer,None)
            #kp2, des2 = orb.detectAndCompute(img,None)
            #print(_count,des1,des2)
           #if des1 is not None and des2 is not None:
           #     matches = bf.match(des1,des2)
           #     #print(np.mean([match.distance for match in matches])*len(matches),_count)
           #     arr.append(np.mean([match.distance for match in matches])*len(matches))
           #     print(_count)
           #     arr_frame.append(_count)

           # _buffer = copy.deepcopy(img)
            print(_count)
    else:
        _buffer = copy.deepcopy(img)
    #print(ret)
    _count +=1
#
#top_distances = np.percentile(arr,90)
#
#distances = [arr.index(distance) for distance in arr if distance > top_distances]
#
#images = [arr_frame[idx]/30 for idx in distances]
#print(images)
