import cv2


img = cv2.imread('handpalm.png')
img = cv2.resize(img,(400,400))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)

canny = cv2.Canny(gray,40,55)

inverted = cv2.bitwise_not(canny)
cv2.imshow('inverted',inverted)
cv2.imwrite('inverted.jpg',inverted)
inverted = cv2.cvtColor(inverted,cv2.COLOR_GRAY2BGR)

cv2.imwrite('inverted.jpg',inverted)

merged = cv2.addWeighted(img,0.5,inverted,0.5,0)
cv2.imshow('merged',merged)
cv2.imwrite('merged.jpg',merged)

cv2.waitKey(0)




