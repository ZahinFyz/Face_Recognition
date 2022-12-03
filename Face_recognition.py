import cv2
import csv
import face_recognition as fr
import numpy as np

name_of_people = []
with open('Facial Data.csv') as data :
    data = csv.reader(data)
    next(data)
    for col in data :
        name_of_people.append(col[0])



#file = open("Facial Data.csv")
#numpy_array = np. loadtxt(file, delimiter=",")
#print(numpy_array)


knownEncodedList = []
with open('Facial Data.csv') as data :
    data = csv.reader(data)
    next(data)
    for col in data :
        encode = np.array(col[1])
        knownEncodedList.append(encode)

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

        #getting the best match
        matchIndex = np.argmin(faceDis)
        z = np.min(faceDis)
        #print(matchIndex)
        if z < 0.45 :
            #Designing the Frame
            if matches[matchIndex]:
                name = name_of_people[matchIndex]
                y1,x2,y2,x1 = facelocF
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1 , y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img , name,(x1+6 , y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                print(name)
        else :
            name = 'Tresspasser'
            y1, x2, y2, x1 = facelocF
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (128,0,0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (128,0,0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)


    cv2.imshow('webcam' ,img)
    cv2.waitKey(1)
