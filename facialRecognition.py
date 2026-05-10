import cv2
from cv2 import CascadeClassifier
from cv2 import rectangle

#STEP 1: read image => imread
#STEP 2: create a classifier and load the xml file to memory => CascaseClassifier(xml file)
#STEP 3: run the algorithm by the image and create the list of features => classifier.detectMultiScale(img)
#STEP 4: draw the boxes over the detected regions => rectangle(img, start , end , color , thickness)

img = cv2.imread('faces2.jpg')

classifier = CascadeClassifier('haarcascade_frontalface_default.xml')
boxes = classifier.detectMultiScale(img)

for box in boxes:
    x,y,width,height = box
    cv2.rectangle(img,(x,y),(x+width,y+height),(255,0,0,0),2)

cv2.imshow('window 1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()