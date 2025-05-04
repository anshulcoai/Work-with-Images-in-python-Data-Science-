import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
img=cv2.imread(r"C:\Users\pc\Downloads\pexels-iriser-1366957.jpg",
               cv2.IMREAD_GRAYSCALE)

output_path = r"C:\Users\pc\Desktop\nature_gray.jpg"
cv2.imwrite(output_path,img)
