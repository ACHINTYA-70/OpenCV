import cv2
import numpy as np

image=cv2.imread("samples/me.jpg",cv2.IMREAD_GRAYSCALE)
# image=cv2.imread("samples/rose.jpg",cv2.IMREAD_GRAYSCALE)

image=cv2.resize(image,(600,550))

# blur = cv2.GaussianBlur(image,(5,5),0)

# edged=cv2.Canny(blur,100,150)

ret, thres_image=cv2.threshold(image,120,255,cv2.THRESH_BINARY)

cv2.imshow("Original Image",image)
# cv2.imshow("blur Image",blur)
# cv2.imshow("Edged Image",edged)
cv2.imshow("thres Image",thres_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
