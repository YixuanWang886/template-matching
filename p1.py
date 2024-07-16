import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
landscape=cv.imread("landscape.jpg",cv.IMREAD_UNCHANGED)
duo=cv.imread("duo.jpg",cv.IMREAD_UNCHANGED)

result=cv.matchTemplate(landscape,duo,cv.TM_CCOEFF_NORMED)

min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)

threshold=0.8
if max_val>=threshold:
    topleft=max_loc
    box_width=duo.shape[1]
    box_height=duo.shape[0]

    bottom_right=(topleft[0]+box_width,topleft[1]+box_height)
    cv.rectangle(landscape,topleft,bottom_right,color=(255,255,255),thickness=2,lineType=cv.LINE_4)



cv.imshow("duo",landscape)
cv.waitKey()