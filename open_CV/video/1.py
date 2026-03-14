import cv2

# # FOR VIDEO
  
# cap=cv2.VideoCapture(0)

# while True:
#     ret,frame=cap.read()
    
#     if not ret:
#         print("Error")
#         break

#     cv2.imshow("webcam feed",frame)

#     if(cv2.waitKey(1) & 0xFF==ord("q")):
#         print("Quitting")
#         break

# cap.release()
# cv2.destroyAllWindows()


# FOR SAVING THE VIDEO
# videoWriter(image,codec,fps,frame_size)

camera=cv2.VideoCapture(0)

w=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
h=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec=cv2.VideoWriter_fourcc(*'XVID')

recorder=cv2.VideoWriter("samples/my_video.avi",codec,30,(w,h))

while True:
    ret,frame=camera.read()

    if not ret:
        print("Error")
        break

    recorder.write(frame)
    cv2.imshow("Live Telecast",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        print("Quitting")
        break

camera.release()
recorder.release()
cv2.destroyAllWindows()