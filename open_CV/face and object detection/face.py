import cv2

# cascadeClassfier loads the trained model
face_cascade=cv2.CascadeClassifier("face and object detection\Haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # detectMultiScale() -> scan and detect objects
    # image, scale factor, minNeighbours 
    faces=face_cascade.detectMultiScale(gray,1.1,5)

    """
    x - how far from left
    y - how far from top
    w - width of face
    h - height of face

    x,y -> top left corner
    x+w,y+h -> bottom right corner

    (100,130,60,70) means

    from (100,130) to (160,200) 
    """ 
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(w+x,h+y),(0,255,0),thickness=6)

    cv2.imshow("Webcam face detection",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()