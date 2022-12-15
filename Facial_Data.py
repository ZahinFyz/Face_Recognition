#importing libraries
import cv2
import glob
import requests
import face_recognition as fr

import numpy as np
import os
import csv
from csv import writer
import pickle




downloaded_images_folder = 'Images'
resized_images_folder = 'Images_r'
x = os.chdir(r"F:\This Semester\Python\Projects\Face Recognition")
binary_images = []
name_of_people = []
knownEncodedList = []

try:
    #Either you make a directory
    os.mkdir(os.path.join(x , resized_images_folder))
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
            name_of_people.append(os.path.splitext(jpg)[0])
            y.append(os.path.splitext(jpg)[0])
            Name  = str(y[0])

            print("No. of image encoded : " + str(q))
            q = q+1
        except :
            pass

pickle.dump(knownEncodedList , open("Face data" , "wb"))
pickle.dump(name_of_people , open("Name data" , "wb"))
print("done Pickling")

#import Face_recognition