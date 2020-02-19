### This will be the combination of color.py and shape.py ###
import cv2
import numpy as np
import argparse
from dictionary import colors
import time

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# print (colors['HSV'])
for color in colors['HSV']:
    # print(colors['HSV'][color])

    boundaries = [colors['HSV'][color]]
    
    for(lower, upper) in boundaries:
        #create NumPy arrays from the boundaries
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")

        #find colors in the bounds and apply mask
        colormask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=colormask)

        #file the images
        timestamp = 'colored/' + color + time.strftime('%H%M%S') + '.jpg'
        # cv2.imwrite(str(path) + str(timestamp), output)
        cv2.imwrite(str(timestamp), output)
        # cv2.imshow("images", np.hstack([image,output]))
        cv2.waitKey(0)


# For loop through the colored folder
# find_shape.py
# end loop
cv2.destroyAllWindows()
