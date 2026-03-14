import cv2

image=cv2.imread("samples/python_image.png")
image2=cv2.imread("samples/me.jpg")
# FOR RESIZEING THE IMAGE

if image is None:
    print("Error")
else:
    print("Success")

    resized=cv2.resize(image,(300,300))
    cv2.imshow("resized image",resized)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
    cv2.imwrite("samples/resized.png",resized)


# FOR CROPPING THE IMAGE

cropped_image=image[100:200,150:550]

cv2.imshow("Cropped image",cropped_image)
cv2.waitKey()
cv2.destroyAllWindows()


# FOR ROTATING THE IMAGE

if image is not None:
    (h,w)=image.shape[:2]

    center=(w//2,h//2)

    a=cv2.getRotationMatrix2D(center,90,0.5)

    rotated_image=cv2.warpAffine(image,a,(w,h))

    cv2.imshow("Rotated image",rotated_image)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("error")


# FOR FLIPPING THE IMAGE
image2=cv2.resize(image2,(500,500))
if image2 is not None:
    flipped_both=cv2.flip(image2,-1)
    cv2.imshow("Flipped image",flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    flipped_horizontal=cv2.flip(image2,1)
    cv2.imshow("Flipped image",flipped_horizontal)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    flipped_vertical=cv2.flip(image2,0)
    cv2.imshow("Flipped image",flipped_vertical)
    cv2.waitKey(0)
    cv2.destroyAllWindows()