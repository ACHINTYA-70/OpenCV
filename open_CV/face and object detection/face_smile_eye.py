import cv2

face_cascade=cv2.CascadeClassifier("face and object detection/Haarcascade_frontalface_default.xml")
smile_cascade=cv2.CascadeClassifier("face and object detection/Haarcascade_smile.xml")
eye_cascade=cv2.CascadeClassifier("face and object detection/Haarcascade_eye.xml")

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face=face_cascade.detectMultiScale(gray,1.1,5)
    
    for(x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]

        upper_gray=roi_gray[0:h//2,:]
        upper_color=roi_color[0:h//2,:]

        eye=eye_cascade.detectMultiScale(upper_gray,1.6,3)
        if len(eye)>0:
            cv2.putText(frame,"Aankhe teri",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
            for(ex,ey,ew,eh) in eye:
                cv2.rectangle(upper_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),3)


        lower_gray=roi_gray[h//2:h,:]
        lower_color=roi_color[h//2:h,:]

        smile=smile_cascade.detectMultiScale(lower_gray,1.6,30)
        if len(smile)>0:
            cv2.putText(frame,"Ahh YESSS",(x,y-50),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
            for(ex,ey,ew,eh) in eye:
                cv2.rectangle(upper_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),3)

    cv2.imshow("Detect this COOL AHH Boy",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


    # spectacles on eyes usnig detecion mka ladle