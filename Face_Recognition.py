#importing libraries
import cv2
import glob
#from PIL import Image
import face_recognition as fr
import numpy as np
import os


inputFolder = 'Images'
pathr = 'Images_r'

bgrImages = []
name_of_people = []

try:
    #Either you make a directory
    os.mkdir(os.path.join(os.getcwd(), pathr))
except:
    pass




#Resizing all images in main folder
'''https://stackoverflow.com/questions/74244841/resizing-a-
folder-of-images-and-saving-it-with-the-same-name-in-a-different-fold'''


p=1
for img in glob.glob(inputFolder + "/*.jpeg"):
    image = cv2.imread(img)
    h = image
    imgResized = cv2.resize(image, (300, 400))
    cv2.imwrite(os.path.join(pathr ,img.split(os.sep)[-1]), imgResized)
    print("No. of image resized : " + str(p))
    p = p+1

jpg_image_list = os.listdir(pathr)
print(jpg_image_list)

q = 1
for jpg in jpg_image_list :
    #reading images using imread() and adding to the empty list images
    #cv2.imread(path, flag)

    bgrImages.append(cv2.imread(f'{pathr}/{jpg}'))
    print("No. of Images Appended : " + str(q))
    q = q+1
    name_of_people.append(os.path.splitext(jpg)[0])



#Generate encoding for the images
def generateEncodings (bgrImages) :
    i = 1
    encodedList = []
    for img in bgrImages:
        encode = fr.face_encodings(img)[0]
        encodedList.append(encode)
        print("encoded" + str(i))
        i = i+1
    return encodedList

knownEncodedList = generateEncodings(bgrImages)
print("Lenght of encoded list : " + str(len(knownEncodedList)))


#Use to get video steam from camera
'''https://www.geeksforgeeks.org/python-opencv-capture-video-
from-camera/#:~:text=Use%20cv2.,the%20frames%20in%20the%20video.'''
cap = cv2.VideoCapture(0)

while True :
    '''https://stackoverflow.com/
    questions/65535939/python-understanding-read-in-opencv'''
    success , img = cap.read()
    #Resiving the image so that it doesn't take much time to read
    imgS = cv2.resize(img,(0,0),None , 0.25 , 0.25)

    facesInF = fr.face_locations(imgS)
    encInF = fr.face_encodings(imgS,facesInF)

    #sequentially grab face locations and face encodings of the video
    for encodeFaceF , facelocF in zip(encInF,facesInF):

        #matching with our given data set
        matches = fr.compare_faces(knownEncodedList , encodeFaceF)
        faceDis = fr.face_distance(knownEncodedList , encodeFaceF)
        print(faceDis)

        #getting the best match
        matchIndex = np.argmin(faceDis)

        #Designing the Frame
        if matches[matchIndex]:
            name = name_of_people[matchIndex]
            y1,x2,y2,x1 = facelocF
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1 , y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img , name,(x1+6 , y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            print(name)

    cv2.imshow('webcam' ,img)
    cv2.waitKey(1)

