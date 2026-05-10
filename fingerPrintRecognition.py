import cv2
from cv2 import *

#STEP 1 read the image => imread
#STEP 2 convert it from bgr to gray => cvtColor(img,cv2.COLOR_BGR2GRAY)
#STEP 3 make a sift feature extractor => SIFT_create()
#STEP 4 extract each keypoint and compute its descriptor => detectAndCompute(img,none)
#STEP 5 draw the keypoints => drawKeyPoints(grayImg , keyPoints, img)

img = cv2.imread('fingerprint1.jpg')
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
keyPoints, descriptors = sift.detectAndCompute(img,None)

siftImage = cv2.drawKeypoints(grayImage , keyPoints , img)

cv2.imshow('window 2',siftImage)
cv2.imshow('window 3',grayImage)
cv2.waitKey(0)
cv2.destroyAllWindows()