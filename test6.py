import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread(r"F:\Data Science\OPen CV Python\nature.jpg",cv2.IMREAD_COLOR)

img2=cv2.copyMakeBorder(img,6,6,6,6,cv2.BORDER_CONSTANT)

cv2.imshow("image:- ",img2)
cv2.waitKey(0)

