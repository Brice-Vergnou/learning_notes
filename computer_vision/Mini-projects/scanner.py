# from https://pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/

# import libraries
import cv2
from transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils

RESIZE = True

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Path to the image to be scanned", required=True)
args = vars(ap.parse_args())
print(f"Test : {ap.parse_args()}   ,   {args}") # first time using it, so i wanna see what it does

#### EDGE DETECTION #####
print("STEP 1 : Edge Detection - Working on it...")
image = cv2.imread(args["image"])
orig = image.copy()
if RESIZE:
    ratio = image.shape[0] / 500
    # should speed up processing, i'll try with and without it
    image = imutils.resize(image, height=500)  


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurring  helps wis with contour detection by removing noise
gray = cv2.GaussianBlur(gray, (7,7), 0)
edged = cv2.Canny(gray, 75, 200)

cv2.imshow("Image", image)
cv2.imshow("Edged", edged)
print("STEP 1: Edge Detection - Done")

#### COUNTOUR DETECTION ####
print("STEP 2 : Contour Detection - Working on it...")
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # find contours
cnts = imutils.grab_contours(cnts) # "unify" the way contours are returned
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5] # keep largest contours

for c in cnts:
    peri = cv2.arcLength(c, True) # get perimeter of a closed shape
    approx = cv2.approxPolyDP(c, 0.02 * peri, True) # approximate the shape
     
    print(f"Peri : {peri}    ,   approx : \n{approx}")

    if len(approx) == 4: # if a shape has 4 edges, we consider it's the document
        screenCnt = approx
        break


print("STEP 2 : Contour Detection - Done")
# draws ALL contours ( -1 ) in green and with a thickness of 2
cv2.drawContours(image, [screenCnt], -1, (0,255,0), 2 ) 
cv2.imshow("Outline", image)

#### PERSPECTIVE WARP & THRESHOLD ####
print("STEP 3 : Rendering - Working on it...")

print(screenCnt.shape)
warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio) # warping transformation
warped2 = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset=10, method="gaussian")
warped = (warped>T).astype("uint8") * 255

print("STEP 3 : Rendering - DONE")
cv2.imshow("Original", imutils.resize(orig, height = 650))
cv2.imshow("Scanned", imutils.resize(warped, height = 650))
cv2.waitKey(0)