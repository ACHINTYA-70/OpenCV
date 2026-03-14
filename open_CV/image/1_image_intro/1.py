import cv2

# LOAD THE IMAGE

image=cv2.imread("samples/python_image.png")

if image is None:
    print("Error")
else:
    print("Success")


# DISPLAY THE IMAGE

if image is not None:
    cv2.imshow("image showing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error")


# SAVE THE IMAGE

if image is not None:
    success=cv2.imwrite("samples/output.jpg",image)
    if success:
        print("image saved succesfully")
    else:
        print("Failed")
else:
    print("error")


# FOR DIMESIONS OF IMAGE

if image is not None:
    h,w,c=image.shape
    print(f"Image loaded:\nheight: {h}\nwidth: {w}\nchannels: {c}")
else:
    print("Error")


# GRAYSCALE CONVERSION

if image is not None:
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    success=cv2.imshow("Grayscale Image",gray)
    cv2.waitKey()
    cv2.destroyAllWindows()
    s2=cv2.imwrite("samples/grayscale.png",gray)
    if s2:
        print("Succesbbcewi")
else:
    print("Error")


# hw
image=cv2.imread("samples/me.jpg")
if image is not None:
    print("image loaded")

    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    print("image converted")

    gray=cv2.resize(gray,(450,500))

    cv2.imshow("image converted to grayscale",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("image showed succesfully")

    cv2.imwrite("samples/me_output.png",gray)
    print("image saved as me_output.png")


else:
    print("Error")


location=input("Enter image location : ")
image=cv2.imread(location)

if image is not None:

    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray=cv2.resize(gray,(500,500))

    a=input("what to do next -> 1 show \n2 Save")

    if(a=="1"):
        cv2.imshow("image",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif(a=="2"):
        b=input("write name for saving the file : ")
        cv2.imwrite(b,gray)
else:
    print("Error")
