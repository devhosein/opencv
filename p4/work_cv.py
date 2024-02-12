# https://www.youtube.com/watch?v=kSqxn6zGE0c
import pandas as pd
import numpy as np
from glob import glob
import cv2
import matplotlib.pylab as plt

# # read the image
# image1 = cv2.imread("A:\Python\MY_projects\opencv\p3\image1.jpg")
# cv2.imshow("iamge", image1)
# cv2.waitKey(5000)


image = cv2.imread("A:\Python\MY_projects\opencv\p4\images.jpg" , cv2.IMREAD_GRAYSCALE)
image = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2BGR)
cv2.imshow("hello", image)
print(f" {image.shape}")
cv2.waitKey(5000)

