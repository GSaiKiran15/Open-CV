import numpy as np
import cv2

img = cv2.imread("tomatoes.jpg")
# cv2.imshow("Img", img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow("hsv", hsv)

h = hsv[:,:,0]
# cv2.imshow('h', h)

# ret, threshold = cv2.threshold(h, 20, 255, cv2.THRESH_BINARY)
# cv2.imshow("thersh", threshold)

ret, threshold = cv2.threshold(h, 25, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow("thershinv", threshold)

edges = cv2.Canny(img, 100, 200, apertureSize=3)
# cv2.imshow("Edges", edges)
edges = 255- edges

kernel = np.ones((2,2), 'uint8')
erode = cv2.erode(edges, kernel, iterations=1)

and_operator = cv2.bitwise_and(erode, threshold)
# cv2.imshow("and", and_operator)

contours, hierarchy = cv2.findContours(and_operator, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

objects = img.copy()

for c in contours:
    if cv2.contourArea(c) > 300:
        cv2.drawContours(objects, [c], -1, (255, 255, 0), 1)
        M = cv2.moments(c)
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])
        cv2.circle(objects, (x,y), 4, (255,0,0), -1)

final = cv2.bitwise_and(objects, img)

cv2.imshow("objects",final)

cv2.waitKey(0)
