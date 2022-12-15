import  cv2
import face_recognition as fr
import numpy as np
import pickle
import csv
from PIL import Image , ImageDraw , ImageFont, ImageFilter





imgBackground = cv2.imread('temp2.png')
imgBackgrounds = cv2.imread('temp4.png')
knownEncodedList = pickle.load(open("Face data" , "rb"))
name_of_people = pickle.load(open("Name data" , "rb"))


#print(knownEncodedList)
#print(name_of_people)
def show_data(name):
    try :
        csv_file = csv.reader(open("Student Database.csv"))
        for row in csv_file:
            if name == row[0]:
                n = 'Name : '+ row[0]
                e = 'Email : '+ row[1]
                i = 'Id : '+ row[2]
                p = 'Phone : '+ row[3]
                return n , e , i, p

                print(x)


    except:
        pass
    try:
        csv_file = csv.reader(open("Faculty Database.csv" , encoding="utf8"))
        for row in csv_file:
            if name == row[0]:
                n = 'Name : ' + row[0]
                e = 'Email : ' + row[1]
                p = 'Phone : ' + row[2]
                d = 'Dept : ' + row[3]
                return n, e, p, d

    except :
        pass


#Use to get video steam from camera
'''https://www.geeksforgeeks.org/python-opencv-capture-video-
from-camera/#:~:text=Use%20cv2.,the%20frames%20in%20the%20video.'''
cap = cv2.VideoCapture(0)




while True :
    def re():
        if z < 0.45:
            imgBackground[100:100+480,720:720+744] = imgBackgrounds
            #imgBackground.paste(imgBackgrounds,(100 , 700))
            # Designing the Frame
            if matches[matchIndex]:
                name = name_of_people[matchIndex]
                y1, x2, y2, x1 = facelocF
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(imgBackground, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(imgBackground, (x1, y2 - 35), (x2, y2), (0, 255, 0))
                # cv2.putText(imgBackground, name,(x1+6 , y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                try:
                    n, e, i, p = show_data(name)
                    cv2.putText(imgBackground, n, (720, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                    cv2.putText(imgBackground, e, (720, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                    cv2.putText(imgBackground, i, (720, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                    cv2.putText(imgBackground, p, (720, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                except:
                    pass
        else :
            imgBackground[100:100 + 480, 720:720 + 744] = imgBackgrounds
            name = 'Tresspasser'
            y1, x2, y2, x1 = facelocF
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(imgBackground, (x1, y1), (x2, y2), (128, 0, 0), 2)
            cv2.rectangle(imgBackground, (x1, y2 - 35), (x2, y2), (128, 0, 0), cv2.FILLED)
            cv2.putText(imgBackground, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            cv2.putText(imgBackground, name, (720, 200), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), 3)


    '''https://stackoverflow.com/
    questions/65535939/python-understanding-read-in-opencv'''
    success , img = cap.read()
    #x = int(float("asdgadg"))
    imgBackground[100:100+480,62:62+640] = img
    #imgBackground[5:5 + 480, 5:5 + 640] = x
    #Resiving the image so that it doesn't take much time to read
    imgS = cv2.resize(imgBackground,(0,0),None , 0.25 , 0.25)

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
        re()


    #cv2.imshow('webcam' ,img)
    cv2.imshow('Face Recognition', imgBackground)
    #cv2.imshow('Face Recognition', "sdgasdfg")

    cv2.waitKey(1)

