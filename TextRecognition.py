import cv2
from cv2 import *
import easyocr

#STEP 1: read the image => cv2.imread()
#STEP 2: initiate the reader => easyocr.Reader(['en'],gpu = False)
#STEP 3: detect and recognize the text and generate the result => reader.readtext(img)
#STEP 4: draw a rectangle arround each detected text => cv2.rectangle(img,p1,p2,color,thickness)
#STEP 5: write the text above the rectangle=> cv2.putText(img,p1,cv2.FONT_HERSHEY_COMPLEX,1,color,thickness)
img = cv2.imread('text1.png')
reader = easyocr.Reader(['en'],gpu= False)

result = reader.readtext(img)
for text in result:
    p1 = text[0][0]
    p2 = text[0][2]
    extractedtext = text[1]
    cv2.rectangle(img,p1,p2,(255,0,0),1)
    cv2.putText(img,extractedtext,p1,cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)


cv2.imshow('text.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

