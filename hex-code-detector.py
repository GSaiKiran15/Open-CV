import webcolors
import cv2
from colour import Color


x_coordinate = 0
y_coordinate = 0

img = cv2.imread("colors.png")

def record_click(event, x, y, flags, param, img=img):
    if event == cv2.EVENT_LBUTTONDOWN:
        x_coordinate = x
        y_coordinate = y
        print(f"Mouse clicked at ({x}, {y})")
        rgb = img[y,x][::-1]
        rgb = (rgb[0], rgb[1], rgb[2])
        hex_color = "#{:02x}{:02x}{:02x}".format(*rgb)
        print(hex_color)
# Find the closest color name
        closest_color = Color(hex_color)
        closest_color = closest_color.get_web()
        print("Closest Color:", closest_color)


cv2.imshow("image", img)

cv2.setMouseCallback('image', record_click)
print(img[x_coordinate, y_coordinate])
cv2.waitKey(0)
cv2.destroyAllWindows()