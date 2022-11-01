#importing libraries
import cv2
import glob
#from PIL import Image
import face_recognition as fr
import numpy as np
import os


path = 'Images'
pathr = 'Images_r'
bgrImages = []
name_of_people = []
#rgbImages = []
jpg_image_list = os.listdir(pathr)
#print(jpg_image_list)

#Resizing all images in main folder
inputFolder = 'Images'

'''https://stackoverflow.com/questions/74244841/resizing-a-
folder-of-images-and-saving-it-with-the-same-name-in-a-different-fold'''
for img in glob.glob(inputFolder + "/*.jpg"):
    image = cv2.imread(img)
    h = image
    imgResized = cv2.resize(image, (300, 400))
    cv2.imwrite(os.path.join('Images_r',img.split(os.sep)[-1]), imgResized)
'''inputFolder = 'Images'

for img in glob.glob(inputFolder + "/*.jpg"):
    image = cv2.imread(img)
    h = image
    imgResized = cv2.resize(image, (300, 400))
    cv2.imwrite('Images_r/image.jpg'  , imgResized)'''

'''for image in os.listdir('./Images'):
    try:
    # Separting the filepath from the image's name
        path, filename = os.path.split(image)
        filename = os.path.splitext(filename)[0]
        image = Image.open('./images/' + image)
        # Resizing the image to a set size.
        edited_image = image.resize((300, 300))'''

'''list_of_images = [i for i in glob.glob(f"{path}/*.jpg")]
for i in list_of_images:
    img = Image.open(i)
    img = img.resize((300, 400), Image.Resampling.LANCZOS)
    img.save('./Images_r/' + i[:-4]+ ".jpg")'''
''''#checking to see if the software can detect images properly
j = cv2.imread('Images_r/Zahin.jpg')
jloc = fr.face_locations(j)[0]
encodej = fr.face_encodings(j)[0]
#print(jloc)
cv2.rectangle(j,(jloc[3],jloc[0]),(jloc[1],jloc[2]),(255,0,255),2)
#cv2.imshow('Zahin' , j)
#cv2.waitKey(0)'''

#After spending roughly 2 hours as why we could not change the color format to RGB
#we realized that the new version of imread() converted the image to RGB by default

for jpg in jpg_image_list :
    #reading images using imread() and adding to the empty list images
    #cv2.imread(path, flag)
    #x = cv2.imread(f'{path}/{jpg}')
    bgrImages.append(cv2.imread(f'{pathr}/{jpg}'))
    name_of_people.append(os.path.splitext(jpg)[0])

#print(name_of_people)
    ###cv2.imshow('rsz_1zahin', x)
    ###cv2.waitKey(0)
    ###cv2.destroyAllWindows()

#cv2.imshow('Zahin' , x)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Generate encoding for the images
def generateEncodings (bgrImages) :
    encodedList = []
    for img in bgrImages:
        encode = fr.face_encodings(img)[0]
        encodedList.append(encode)
    return encodedList

knownEncodedList = generateEncodings(bgrImages)
#print(len(knownEncodedList))


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


'''for bgr in bgrImages :
    y = cv2.cvtColor(bgr , cv2.COLOR_BGR2RGB)
    rgbImages.append(cv2.cvtColor(bgr , cv2.COLOR_BGR2RGB))
    ###cv2.imshow('rsz_1zahin', y)
    ###cv2.waitKey(0)
    ###cv2.destroyAllWindows()'''
