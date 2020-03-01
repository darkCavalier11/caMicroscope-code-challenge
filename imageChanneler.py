import sys
import cv2 as cv
import numpy as np
image_path = 'views/uploads/image.jpg'
img = cv.imread(image_path, 1)
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
cv.imwrite('views/uploads/image_green.jpg', g)
cv.imwrite('views/uploads/image_red.jpg', r)
cv.imwrite('views/uploads/image_blue.jpg', b)
print('Done')