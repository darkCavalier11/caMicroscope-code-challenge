import cv2 as cv
import numpy as np
image_path = 'views/uploads/image.jpg'
img = cv.imread(image_path, 1)
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
a = np.ones(b.shape, dtype=b.dtype)*50
bg_merge = cv.merge((b,g,a))
gr_merge = cv.merge((g,r,a))
rb_merge = cv.merge((r,b,a))
bgr_merge = cv.merge((b,g,r,a))
cv.imwrite('views/uploads/bg_merge.jpg',bg_merge)
cv.imwrite('views/uploads/gr_merge.jpg',gr_merge)
cv.imwrite('views/uploads/rb_merge.jpg',rb_merge)
cv.imwrite('views/uploads/bgr_merge.jpg', bgr_merge)