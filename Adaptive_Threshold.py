import numpy as np
import cv2

img = cv2.imread("sudoku.png", 0)
cv2.imshow("img", img)
a_threshold_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow("Adapted", a_threshold_img)
cv2.waitKey(0)
