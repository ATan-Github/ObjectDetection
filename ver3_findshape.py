import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap. add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

kernel = np.ones((3,3), np.uint8)

boundaries = [([165, 27, 74], [259, 255, 255])]
for(lower, upper) in boundaries:
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
    colormask = cv2.inRange(image, lower, upper)
    colormask_eroded = cv2.erode(colormask, kernel)

opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
contours, hierarchy2 = cv2.findContours(colormask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


c = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(c)
cv2.rectangle(image,(x,y), (x+w, y+h), (0, 255, 0), 2)
approx = cv2.approxPolyDP(c, 0.1*cv2.arcLength(c, True), True)
if len(approx) == 5:
    print("pentagon")
    cv2.drawContours(image, c, 0, 255, -1)
elif len(approx) == 4:
    print("rectangle")
    cv2.drawContours(image, c, 0, (0, 0, 255), -1)
elif len(approx) == 3:
    print("triangle")
    cv2.drawContours(image, c, 0, (0, 255, 0), -1)
elif len(approx) == 9:
    print("half-circle")
    cv2.drawContours(image, c, 0, (255, 255, 0), -1)
elif len(approx) >15:
    print ("circle")
    cv2.drawContours(image, c, 0, (0, 255, 255), -1)

cv2.imwrite("shapedimage.jpg", image)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
