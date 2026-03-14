import cv2
import numpy as np
# Gaussion Blur = smooth , reduce sharpness

image=cv2.imread("samples/pahad.jpg")
image=cv2.resize(image,(600,450))

blurred=cv2.GaussianBlur(image,(7,7),0)

# cv2.imshow("original image",image)
# cv2.imshow("blurred image",blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Median Blur = smooth, removie noisy use in challan system so can only focus on numberplate not on noisy 

image=cv2.imread("samples/noisy.jpg")

blurred2=cv2.medianBlur(image,3)

# cv2.imshow("original image",image)
# cv2.imshow("blurred image",blurred2)

cv2.imwrite("samples/noisy_op.jpg",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Sharpening Filter

image=cv2.imread("samples/rose.jpg")

kernel=np.array([
    [0 ,-1, 0],     
    [-1, 5,-1],
    [0 ,-1, 0]
])

ddepth=-1

sharpen=cv2.filter2D(image,ddepth,kernel)

cv2.imshow("original image",image)
cv2.imshow("sharped image",sharpen)

cv2.waitKey(0)
cv2.destroyAllWindows()