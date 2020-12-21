import cv2

img=cv2.imread('pic3.jpg')

img_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('HSV Image',img_HSV)
cv2.waitKey(0)
cv2.imshow("Hue Channel",img_HSV[:,:,0])
cv2.waitKey(0)
cv2.imshow("Saturation Channel",img_HSV[:,:,1])
cv2.waitKey(0)
cv2.imshow("Value Channel",img_HSV[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()

#tinyurl.com/persie12
#haarcascade algorithm