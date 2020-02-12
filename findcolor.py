### All color codes are in hsv format ###
import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #Converts RGB to HSV

# image = cv2.imread('testim.png')

# boundaries = [([100, 50, 0], [255, 180, 104])] #RGB Space

# boundaries = [([163, 56, 74], [179, 255, 255])] #HSV Space
# boundaries = [([11, 153, 172], [24, 255, 255])]
boundaries = [([25, 91, 234], [31, 255, 255])]


for(lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    #find colors in boundaries and apply mask
    colormask = cv2.inRange(image, lower, upper)

    output = cv2.bitwise_and(image, image, mask=colormask)

    # show the images
    cv2.imwrite("coloredimg.jpg", output)
    cv2.imshow("images", np.hstack([image,output]))
    cv2.waitKey(0)

