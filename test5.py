import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread(r"C:\Users\pc\Downloads\95d95c65-b5c4-453c-b744-45db067b8e9e.jpg",cv2.IMREAD_COLOR)
cv2.imshow("image:- ",img)
cv2.waitKey(0)

gs=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("image:- ",gs)
cv2.waitKey(0)

ms=cv2.medianBlur(img,5)
cv2.imshow("image:- ",ms)
cv2.waitKey(0)

bs=cv2.bilateralFilter(img,8,75,75)
cv2.imshow("image:- ",bs)
cv2.waitKey(0)

cv2.destroyAllWindows()
