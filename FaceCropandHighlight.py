""" 
##*********************************************************************************************************
                        Created on Fri Sep  6 21:39:51 2019
                        @Project : Face Detection and Corp 
                        @author  : Parthiban
##*********************************************************************************************************
"""
##CMD Function Call - python "C:\Users\kurnia\Desktop\Python\FaceCropandHighlight.py" "C:/Users/kurnia/Desktop/Face_detection_images/face1.jpg" "mode"  ## mode=portrait/face


import cv2
import sys
import numpy as np
import time
import PIL

#--------------------Directory for images folder---------
import os

dic="C:\\Users\\kurnia\\Desktop\\Face_detection_images -Test"

directory = os.fsencode(dic)

#--------------------------------------------------------

def cropImage(imgPath):
    
    image = cv2.imread(imgPath) 
      
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=3,
        minSize=(30, 30)
    )
    
    print("[INFO] Found {0} Faces.".format(len(faces)))
    
    flgface=False
    flgeye=False
    
    for (x, y, w, h) in faces:
        flgface=True
        #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #padding = 70
        #cv2.rectangle(image,(x-padding,y-padding),(x+w+padding,y+h+padding),(0,255,0),2)
        #roi_color = image[y:y + h+70, x:x + w+40] 
        try:
            x_inc = int(w*0.3)
            y_inc = int(h*0.35)
            sub_face = image[y-y_inc:y+h+y_inc, x-x_inc:x+w+x_inc]
            roi_color = cv2.resize(sub_face,(int(224),int(224))) 
        except:
            print ("Unexpected error:", sys.exc_info()[0])
            try:
                #If enable rectancle code model will mark the face
                #padding = 70
                #cv2.rectangle(image,(x-padding,y-padding),(x+w+padding,y+h+padding),(0,255,0),2)
                roi_color = image[y:y + h+70, x:x + w+40] 
            except:
                print ("Unable to find faces:", sys.exc_info()[0])
                
        print("[INFO] Object found. Saving locally.")
        cropimage='C:\\Users\\kurnia\\Desktop\\Face_detection_images -Test\\Output\\'+str(w) + str(h) + '_faces.jpg'
        cv2.imwrite('C:\\Users\\kurnia\\Desktop\\Face_detection_images -Test\\Output\\'+str(w) + str(h) + '_faces.jpg', roi_color)
        
        list_im = [imgPath, cropimage]
        imgs    = [ PIL.Image.open(i) for i in list_im ]
        # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
        min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
        imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
        
        # save that beautiful picture
        imgs_comb = PIL.Image.fromarray( imgs_comb)
        imgs_comb.save( 'Trifecta.jpg' )
        
        image = cv2.imread('Trifecta.jpg')
        cv2.imshow('image', image);
        cv2.waitKey(0); 
        cv2.destroyAllWindows(); 
        cv2.waitKey(1)
            
        
#        # for a vertical stacking it is simple: use vstack
#        imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
#        imgs_comb = PIL.Image.fromarray( imgs_comb)
#        imgs_comb.save( 'Trifecta_vertical.jpg' )
#        
#        image = cv2.imread('Trifecta_vertical.jpg')
#        cv2.imshow('image', image);
#        cv2.waitKey(0); 
#        cv2.destroyAllWindows(); 
#        cv2.waitKey(1)
#        con=np.concatenate((imgPath,'C:\\Users\\kurnia\\Desktop\\Face_detection_images -Test\\Output\\'+str(w) + str(h) + '_faces.jpg'),axis=1)
#        
#        cv2.imshow('image',con)
#        
#        time.sleep(0.10)
#        variable = raw_input('input something!: ')
#        print(variable)      
#        
                 #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
        #cv2.imshow("cropped", roi_color)
        
        #roi_color = image[y:y + h, x:x + w] 
        
        #cv2.imshow("cropped", roi_color)
       #----------------------------------------------------------------------------------------------------------------- 
#        for (x,y,w,h) in faces:
#             #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#             roi_gray = gray[y:y+h, x:x+w]
#             roi_color = image[y:y+h, x:x+w]
#             eyes = eye_cascade.detectMultiScale(roi_gray)
#             for (ex,ey,ew,eh) in eyes:
#                 print("eye")
#                 flgeye=True
#        
#        #roi_color = image[0:400, 0:300] # Crop from {x, y, w, h } => {0, 0, 300, 400} ##https://stackoverflow.com/questions/45726646/basic-python-opencv-cropping-and-resizing
#        if (flgface==True and flgeye==True):
#            print("[INFO] Object found. Saving locally.")
#            cv2.imwrite('C:\\Users\\kurnia\\Desktop\\Face_detection_images -Test\\Output\\old\\'+str(w) + str(h) + '_faces.jpg', roi_color)
#        else:
#            print("No Eye detected")
        
##        break
        #-----------------------------------------------------------------------------------------------------------------
        #con=np.concatenate((imgPath,'C:\\Users\\kurnia\\Desktop\\Face_detection_images\\'+str(w) + str(h) + '_faces.jpg'),axis=1)
        
        #cv2.imshow('image',con)
    
    #status = cv2.imwrite('faces_detected.jpg', image)
    #status = cv2.imwrite('C:\\Users\\kurnia\\Desktop\\obama.jpg', image)
    #status = cv2.imwrite('C:\\Users\\kurnia\\Desktop\\edit1.jpeg', image)
    #cv2.imshow('image',image)
    #print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
#    
#if __name__ == '__main__':
#    imgPath = sys.argv[1]
#   # mode = sys.argv[2]
#    print(imgPath)
#    #print(mode)
#    cropImage(imgPath)
    
##C:\Users\kurnia>python "C:\Users\kurnia\Desktop\Python\FaceCropandHighlight.py" cropImage "C:\\Users\\kurnia\\Desktop\\face1.jpg"
#cropImage("C:\\Users\\kurnia\\Desktop\\Face_detection_images\\face1.jpg")


#-----------------Images iteration and call face detection function----


for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".jpg") or filename.endswith(".jpeg"): 
         print(dic+"\\"+filename)
         cropImage(dic+"\\"+filename)
         continue
     else:
         continue

























