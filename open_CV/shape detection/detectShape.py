import cv2

# image=cv2.imread("shape detection/shape.png")
image=cv2.imread("shape detection/circle.png")
# image=cv2.imread("samples/pahad.jpg")

image=cv2.resize(image,(600,450))

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

_,thres=cv2.threshold(gray,200,250,cv2.THRESH_BINARY)

contours,hierarchy=cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(image,contours,-1,(0,255,0),5)

for contour in contours:
    approx=cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour,True),True)
    corner=len(approx)
    if(corner==3):
        shape_name="triangle"
    elif(corner==4):
        shape_name="rectangle"
    elif(corner==5):
        shape_name="pentagon"
    elif(corner>5):
        shape_name="circle"
    else:
        shape_name="unknown"

    cv2.drawContours(image,[approx],0,(0,255,0),4)
    x=approx.ravel()[0]
    y=approx.ravel()[1]-10
    cv2.putText(image,shape_name,(x,y),cv2.FONT_HERSHEY_COMPLEX,1.2,(255,0,0),2)

cv2.imshow("Contours",image)
cv2.waitKey(0)
cv2.destroyAllWindows()