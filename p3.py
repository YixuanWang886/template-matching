import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
def templete_matching(templete,item,match_type,threshold=0.5,):
    landscape=cv.imread(templete,cv.IMREAD_UNCHANGED)
    duo=cv.imread(item,cv.IMREAD_UNCHANGED)
    #image.shape:height, width,channel

    result=cv.matchTemplate(landscape,duo,cv.TM_CCOEFF_NORMED)

    min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)

    threshold=0.5

    targets=np.where(result>=threshold)

    targets=list(zip(*targets[::-1]))

    rectangles=[]
    for target in targets:
        x=int(target[0])
        y=int(target[1])
        w=int(duo.shape[0])
        h=int(duo.shape[1])
        rec=(x,y,w,h)
        rectangles.append(rec)

    rectangles_grouped,weights=cv.groupRectangles(rectangles,1,0.5)
    #rec—_group, min_element, strickness(bigger is stricter)
    print(len(rectangles_grouped))

    for rec in rectangles_grouped:
        if match_type=="box":
            top_left=rec[:2]
            bottom_right=(top_left[0]+duo.shape[0],top_left[1]+duo.shape[1])
            cv.rectangle(landscape,top_left,bottom_right,color=(255,255,255),thickness=1,lineType=cv.LINE_4)
        if match_type=="cross":
            center_x=rec[0]+int(rec[2]/2)
            center_y=rec[1]+int(rec[3]/2)
            cv.drawMarker(landscape,(center_x,center_y),(255,0,255),markerType=cv.MARKER_CROSS)

    cv.imshow("res",landscape)
    cv.waitKey()


templete_matching("landscape.jpg",'duo.jpg',"cross")