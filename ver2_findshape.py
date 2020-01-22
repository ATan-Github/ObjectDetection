import cv2
import argparse
import numpy as np

font = cv2.FONT_HERSHEY_COMPLEX

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)
# image = cv2.imread("coloredimg.jpg", cv2.IMREAD_GRAYSCALE)
_, threshold = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("shapes",image)
cv2.waitKey(0)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(image, [approx], 0, (0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 2:
        cv2.putText(image, "Semicircle", (x, y,), font, 1, (0))
    elif len(approx) == 3:
        cv2.putText(image, "Triangle", (x, y), font, 1, (0))
    elif len(approx) == 4:
        cv2.putText(image, "Rectangle", (x, y), font, 1, (0))
    elif len(approx) == 5:
        cv2.putText(image, "Pentagon", (x, y), font, 1, (0))
    elif len(approx) == 6:
        cv2.putText(image, "Hexagon", (x, y), font, 1, (0))
    elif len(approx) == 8:
        cv2.putText(image, "Octagon", (x, y), font, 1, (0))
    else:
        cv2.putText(image, "Circle", (x, y), font, 1, (0))

cv2.imshow("shapes",image)
cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()


