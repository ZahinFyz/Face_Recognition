from bs4 import BeautifulSoup
import requests
from csv import writer
import csv
import os
import pandas as pd

url = "https://zahinfyz.github.io/Nsu-Student-Database.github.io/"

request_web_page = requests.get(url)
soup = BeautifulSoup(request_web_page.text , 'html.parser')
#print(soup)


#First Task get all the images
images = soup.find_all('img')

#making or directring to existing folder
try:
    #Either you make a directory
    os.mkdir(os.path.join(os.getcwd(), 'Images'))
except:
    pass
#Or write to an existing one
os.chdir(os.path.join(os.getcwd(), 'Images'))

#looping to get image name and the image
for image in images :
    #ekhane amra name nicchi of the person from src
    name = image['src'][9:-5]
    #jehetu website ei images gula and prottek ta image er different link
    #tai common part of the link likhe , specific emage tag add kortesi "image['src'][1:23]"
    # 1 ro 23 cause name can be big smaller values can be used
    link = 'https://zahinfyz.github.io/Nsu-Student-Database.github.io'+image['src'][1:23]

    #writing the images in the folder
    with open(name + '.jpeg', 'wb') as f:
        im = requests.get(link)
        f.write(im.content )
        print('Downloaded Image :', name)


os.chdir(r"F:\This Semester\Python\Projects\Face Recognition")

lists = soup.find_all('td')

with open('Student Database.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Sl', 'Image', 'Name', 'Email' , 'ID','Phone']
    thewriter.writerow(header)
    i = 0
    for list in range(500):
        sl = lists[i].text
        i = i+1 ;
        image = lists[i].text
        i = i + 1;
        name = lists[i].text
        i = i + 1;
        email = lists[i].text
        i = i + 1;
        id = str(lists[i].text)
        i = i + 1;
        phone = lists[i].text
        i = i + 1;

        info = [sl , image , name , email , id, phone]
        thewriter.writerow(info)

f=pd.read_csv("Student Database.csv")
keep_col = ['Name','Email','ID','Phone']
new_f = f[keep_col]
new_f.to_csv("Student Database.csv", index=False)

#import Facial_Data