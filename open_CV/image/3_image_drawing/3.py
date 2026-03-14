import cv2

image=cv2.imread("samples/pahad.jpg")
image=cv2.resize(image,(600,450))

# FOR DRAWING A LINE

if image is not None:
    pt1=(100,100)
    pt2=(200,300)
    line=cv2.line(image,pt1,pt2,color=(255,0,0),thickness=4)

    cv2.imshow("Draw line",line)
    cv2.waitKey(0)
    cv2.destroyAllWindows
else:
    print("Regret")


# FOR DRAWING A RECTANGLE

if image is not None:
    pt1=(100,50)
    pt2=(250,100)
    rectangle=cv2.rectangle(image,pt1,pt2,color=(255,0,0),thickness=4)

    cv2.imshow("Draw rectangle",rectangle)
    cv2.waitKey(0)
    cv2.destroyAllWindows
else:
    print("Regret")


# FOR DRAWING A circle

if image is not None:
    center=(300,225)
    radius=200
    rectangle=cv2.circle(image,center,radius,color=(255,0,0),thickness=4)

    cv2.imshow("Draw circle",rectangle)
    cv2.waitKey(0)
    cv2.destroyAllWindows
else:
    print("Regret")


# FOR ADD TEXT 
if image is not None:
    text_add=cv2.putText(image,text="ACHINTYA HOON",org=(100,300),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1.2,color=(255,0,0),thickness=2)
    cv2.imshow("Draw circle",text_add)
    cv2.waitKey(0)
    cv2.destroyAllWindows
else:
    print("Regret")


# hw

location=input("Enter image location : ")

image=cv2.imread(location)

image=cv2.resize(image,(600,450))

if image is not None:
    a=input("what to do next -> 1 line \n2 rectangle \n3 circle \n4 text")

    if(a=="1"):
        print("u need line on ur image ... tell the positions ")
        pt1_x=int(input("tell point1 in tuple : "))
        pt1_y=int(input("tell point1 in tuple : "))
        pt2_x=int(input("tell point1 in tuple : "))
        pt2_y=int(input("tell point2 in tuple : "))
        pt1=(pt1_x,pt1_y)
        pt2=(pt2_x,pt2_y)
        cv2.line(image,pt1,pt2,color=(0,225,0),thickness=6)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif(a=="2"):
        print("u need rectangle on ur image ...  done rectangle")
        pt1_x=int(input("tell point1 in tuple : "))
        pt1_y=int(input("tell point1 in tuple : "))
        pt2_x=int(input("tell point1 in tuple : "))
        pt2_y=int(input("tell point2 in tuple : "))
        pt1=(pt1_x,pt1_y)
        pt2=(pt2_x,pt2_y)
        cv2.line(image,pt1,pt2,color=(0,225,0),thickness=6)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif(a=="3"):
        print("u need circle on ur image ...  done circle")
        pt1_x=int(input("tell point1 in tuple : "))
        pt1_y=int(input("tell point1 in tuple : "))
        center=(pt1_x,pt1_y)
        radius=input("tell radius :")
        cv2.circle(image,center,radius,color=(0,225,0),thickness=6)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif(a=="4"):
        print("u need puttext on ur image ...  done puttext")    
        text=input("tell the text in string : ")  
        pt1_x=int(input("tell point1 in tuple : "))
        pt1_y=int(input("tell point1 in tuple : ")) 
        org=(pt1_x,pt1_y)
        cv2.putText(image,text,org,font=cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(0,225,0),thickness=6)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

else:
    print("Error")