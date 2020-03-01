import sys
import cv2 as cv
import numpy as np
image_path = './uploads/{0}'.format(sys.argv[1])
img = cv.imread(image_path, 1)
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
cv.imwrite('./uploads/{0}_green.jpg'.format(sys.argv[1]), g)
cv.imwrite('./uploads/{0}_red.jpg'.format(sys.argv[1]), r)
cv.imwrite('./uploads/{0}_blue.jpg'.format(sys.argv[1]), b)
print('Done!')
