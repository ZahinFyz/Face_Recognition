#importing libraries
import cv2
import glob
import requests
import face_recognition as fr
import numpy as np
import os
import csv
from csv import writer


downloaded_images_folder = 'Images'
resized_images_folder = 'Images_r'

binary_images = []
name_of_people = []
knownEncodedList = []

try:
    #Either you make a directory
    os.mkdir(os.path.join(os.getcwd(), resized_images_folder))
except:
    pass


#Resizing all images in main folder
'''https://stackoverflow.com/questions/74244841/resizing-a-
folder-of-images-and-saving-it-with-the-same-name-in-a-different-fold'''


p=1
for img in glob.glob(downloaded_images_folder + "/*.jpeg"):
    try :
        #First a amra downloaded image folder a dhuki
        #then one by one we resize the images
        #then savve them to resized image folder
        image = cv2.imread(img)
        h = image
        imgResized = cv2.resize(image, (300, 400))
        cv2.imwrite(os.path.join(resized_images_folder, img.split(os.sep)[-1]), imgResized)
        print("No. of image resized : " + str(p))
        p = p+1
    except:
        pass

try:
    #making a list of the names in resized images folder
    # os.listdir() :list of names of all the files present in the specified path
    list_of_names_in_resized_image_folder = os.listdir(resized_images_folder)
except:
    pass

def write_data() :
    os.chdir(r"F:\This Semester\Python\Projects\Face Recognition")
    info = [Name, Data]
    thewriter.writerow(info)

with open('Facial Data.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Name', 'Data' ]
    thewriter.writerow(header)


    q = 1
    for jpg in list_of_names_in_resized_image_folder :
        #Ekta temporary list banailam
        x = []

        x.append(cv2.imread(f'{resized_images_folder}/{jpg}'))
        #Temporary list tai ekta binary image nilam

        #Ekhon amra oi temoporary list tai dhukbo
        #First kaj hocche facial encodings nawa jai naki check kora
        #Jodi encode kora jai then append the name of the person
        for img in x:
            try :
                y = []
                encode = np.array(fr.face_encodings(img)[0])
                knownEncodedList.append(encode)
                Data = encode
                print(Data.shape)
                #binary_images.append(cv2.imread(f'{resized_images_folder}/{jpg}'))
                name_of_people.append(os.path.splitext(jpg)[0])
                y.append(os.path.splitext(jpg)[0])
                #print(type(str(y)))
                Name  = str(y[0])
                #print(Name)
                print("No. of Images Appended : " + str(q))
                q = q+1

                write_data()
            except :
                pass

print("Lenght of encoded list : " + str(len(knownEncodedList)))
print(knownEncodedList[0].shape)
print(type(knownEncodedList))
print(name_of_people[0])
print(type(name_of_people))


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
