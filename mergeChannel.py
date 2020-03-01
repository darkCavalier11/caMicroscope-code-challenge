import sys
import cv2 as cv
import numpy as np
blue_channel = cv.imread('views/uploads/image_blue.jpg')
green_channel = cv.imread('views/uploads/image_green.jpg')
red_channel = cv.imread('views/uploads/image_red.jpg')
bg_merge = cv.merge((blue_channel, green_channel))
gr_merge = cv.merge((green_channel, red_channel))
rb_merge = cv.merge((red_channel, blue_channel))
bgr_merge = cv.merge((blue_channel, green_channel, red_channel))
cv.imwrite('views/uploads/bg_merge.jpg',bg_merge)
cv.imwrite('views/uploads/gr_merge.jpg',gr_merge)
cv.imwrite('views/uploads/rb_merge.jpg',rb_merge)
cv.imwrite('views/uploads/bgr_merge.jpg',bgr_merge)