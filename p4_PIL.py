import PIL.ImageGrab
import cv2 as cv
import numpy as np
import os
import PIL
from time import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))

loop_time=time()
while True:
    screenshot=PIL.ImageGrab.grab()
    cv_image=np.array(screenshot)
    cv_image=cv.cvtColor(cv_image,cv.COLOR_RGB2BGR)
    cv.imshow("screen",cv_image)

    print('FPS{}'.format(1/(time()-loop_time)))
    loop_time=time()
    if cv.waitKey(1)==ord("q"):
        break

cv.destroyAllWindows()