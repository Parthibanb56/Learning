#Python 2.7.2
#Opencv 2.4.2
#PIL 1.1.7

import cv2
#import Image
from PIL import Image

print ("1")

def DetectFace(image, faceCascade):
    #modified from: http://www.lucaamore.com/?p=638

    min_size = (20,20)
    image_scale = 1
    haar_scale = 1.1
    min_neighbors = 3
    haar_flags = 0

    # Allocate the temporary images
    smallImage = cv2.CreateImage(
            (
                cv2.Round(image.width / image_scale),
                cv2.Round(image.height / image_scale)
            ), 8 ,1)

    # Scale input image for faster processing
    cv2.Resize(image, smallImage, cv2.CV_INTER_LINEAR)

    # Equalize the histogram
    cv2.EqualizeHist(smallImage, smallImage)

    # Detect the faces
    faces = cv2.HaarDetectObjects(
            smallImage, faceCascade, cv2.CreateMemStorage(0),
            haar_scale, min_neighbors, haar_flags, min_size
        )

    # If faces are found
    if faces:
        for ((x, y, w, h), n) in faces:
            # the input to cv.HaarDetectObjects was resized, so scale the
            # bounding box of each face and convert it to two CvPoints
            pt1 = (int(x * image_scale), int(y * image_scale))
            pt2 = (int((x + w) * image_scale), int((y + h) * image_scale))
            cv2.Rectangle(image, pt1, pt2, cv2.RGB(255, 0, 0), 5, 8, 0)

    return image

print ("#2")

def pil2cvGrey(pil_im):
    #from: http://pythonpath.wordpress.com/2012/05/08/pil-to-opencv-image/
    pil_im = pil_im.convert('L')
    cv_im = cv2.CreateImageHeader(pil_im.size, cv2.cv.IPL_DEPTH_8U, 1)
    cv2.SetData(cv_im, pil_im.tostring(), pil_im.size[0]  )
    return cv_im

print ("3")

def cv2pil(cv_im):
    return Image.fromstring("L", cv2.GetSize(cv_im), cv_im.tostring())

print ("4")

pil_im=Image.open('C:/Users/kurnia/Desktop/barackobama.jpg')
#pil_im.show()
cv_im=pil2cvGrey(pil_im)
#the haarcascade files tells opencv what to look for.
faceCascade = cv2.Load('C:/Users/kurnia/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
face=DetectFace(cv_im,faceCascade)
img=cv2pil(face)
img.show()