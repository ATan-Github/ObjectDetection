import cv2

class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, c):
        #initialize the shape name and approximate the contour
        shape = "unidentified"
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04*perimeter, True)

        #semicircle
        if len(approx) == 2:
            shape = "semicircle"

        #triangle
        elif len(approx) == 3:
            shape = "triangle"

        #quadrilateral
        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w/float(h)

            shape = "square" if ar>=0.95 and ar<=1.05 else "rectangle"

        #pentagon
        elif len(approx) == 5:
            shape = "pentagon"
        #octagon
        elif len(approx) == 8:
            shape = "octagon"

        else:
            shape = "circle"

        return shape

