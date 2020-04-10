import cv2
import argparse
import imutils
from Shape_Detector import ShapeDetector

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
# image = cv2.imread("coloredimg.jpg")

cv2.imshow("original image", image)
cv2.waitKey(0)

#resizing image to process shapes accurately
# resized = imutils.resize(image, width=300)
# ratio = image.shape[0] / float(resized.shape[0])

#grayscaling, blurring, and thresholding
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("resized", gray)
cv2.waitKey(0)
blurred = cv2.GaussianBlur(gray, (5, 5),0)
cv2.imshow("blurred", blurred)
cv2.waitKey(0)
thresh = cv2.threshold(blurred, 50, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("threshold", thresh)
cv2.waitKey(0)

#find contours and initialize ShapeDetector
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
#TEsting
cv2.drawContours(thresh, contours, -1, [255, 255, 255], thickness = cv2.FILLED)
cv2.imshow("filled", thresh)
cv2.waitKey(0)

contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

shape = ShapeDetector()

#loop the contours
for contour in contours:
    #compute the center and detect the shape with only contours
    M = cv2.moments(contour) #moments
    # conX = int((M["m10"] / (M["m00"]+0.00000001)) * ratio) #contourX
    # conY = int((M["m01"] / (M["m00"]+0.00000001)) * ratio) # contourY
    conX = int((M["m10"] / (M["m00"]+0.00000001)) ) #contourX
    conY = int((M["m01"] / (M["m00"]+0.00000001)) ) # contourY
    shape = shape.detect(contour)

#multiply the contour coordinate by the resize ratio then draw the contours on the name of the shape on the image
contour = contour.astype("float")
# contour *= ratio
contour = contour.astype("int")
cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
cv2.putText(image, shape, (conX, conY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

#output image
cv2.imwrite("shapedimage.jpg", image)
cv2.imshow("Image", image)
cv2.waitKey(0)
