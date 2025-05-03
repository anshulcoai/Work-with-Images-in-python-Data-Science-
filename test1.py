import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\\pc\\Downloads\\pexels-maxime-francis-2246476(1).jpg", cv2.IMREAD_COLOR)

if img is None:
    print("Failed to load image. Check the file path.")
else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB for matplotlib
    plt.imshow(img)
    plt.waitforbuttonpress()
    plt.close('all')
