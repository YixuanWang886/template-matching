import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
landscape=cv.imread("landscape.jpg",cv.IMREAD_UNCHANGED)
duo=cv.imread("duo.jpg",cv.IMREAD_UNCHANGED)

result=cv.matchTemplate(landscape,duo,cv.TM_CCOEFF_NORMED)

min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)

threshold=0.5

targets=np.where(result>=threshold)

targets=list(zip(*targets[::-1]))
print(len(targets))

for target in targets:
    top_left=target
    bottom_right=(top_left[0]+duo.shape[0],top_left[1]+duo.shape[1])
    cv.rectangle(landscape,top_left,bottom_right,color=(255,255,255),thickness=1,lineType=cv.LINE_4)

cv.imshow("res",landscape)
cv.waitKey()
