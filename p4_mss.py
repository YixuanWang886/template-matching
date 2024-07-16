import PIL.ImageGrab
import cv2 as cv
import numpy as np
import os
import mss
from time import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))

loop_time=time()
while True:
    with mss.mss() as sct:
        screenshot_path = sct.shot()
        cv_image = cv.imread(screenshot_path)  # Read the screenshot into a NumPy array
        cv.imshow("screen", cv_image)

        print('FPS{}'.format(1 / (time() - loop_time)))
        loop_time = time()
        if cv.waitKey(1) == ord("q"):
            break

cv.destroyAllWindows()