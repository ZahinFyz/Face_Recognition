from tkinter import *
from PIL import Image
import time
import threading

app = Tk()



#Interface Geometry
app.geometry("1280x800")
app.resizable(False , False)
app.config(background = 'black')

#Frames
data_frame = Frame(app , height=1280 , width= 350 , bg= "#156286" , bd = 2 ,relief= RAISED)
data_frame.place(x=0 , y=0)

#Gif
file = "giphy.gif"

info = Image.open(file)

frames = info.n_frames
#print(frames)

# creating list of PhotoImage objects for each frames
im = [PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = app.after(50,lambda :animation(count))

gif_label = Label(image="")
gif_label.place(x= 550 , y = 200)

animation(count)

#Texts
welcome = Label(text="Hello I am Vision !! " , fg = "white" , bg = 'black' , font = "Arial 40 bold")
welcome.place(x= 600 , y = 50)

question = Label(text="What would you like  " , fg = "black" , bg = '#156286' , font = "Arial 20 bold")
question.place(x= 25 , y = 200)
question1 = Label(text="me to do ?? " , fg = "black" , bg = '#156286' , font = "Arial 20 bold")
question1.place(x= 25 , y = 250)


def face():
    import Face_recognition
    app.destroy()

def face_encoding():
    import Facial_Data
    face()

def encode():
    for widget in app.winfo_children():
        widget.destroy()
    # Interface Geometry
    app.geometry("1280x800")
    app.resizable(False, False)
    app.config(background='black')

    # Frames
    data_frame = Frame(app, height=1280, width=350, bg="#156286", bd=2, relief=RAISED)
    data_frame.place(x=0, y=0)

    ######################Gif
    file = "giphy.gif"

    info = Image.open(file)

    frames = info.n_frames
    # print(frames)

    # creating list of PhotoImage objects for each frames
    im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

    coun = 0
    anim = None

    def animatio(coun):
        global anim
        im2 = im[coun]

        gif_label.configure(image=im2)
        coun += 1
        if coun == frames:
            coun = 0
        anim = app.after(50, lambda: animatio(coun))

    gif_label = Label(image="")
    gif_label.place(x=550, y=200)

    animatio(coun)
    # Gif Ends############################################

    # Texts
    welcome = Label(text="Encoding Data !! ", fg="white", bg='black', font="Arial 40 bold")
    welcome.place(x=600, y=50)

    question = Label(text="Please wait while", fg="black", bg='#156286', font="Arial 20 bold")
    question.place(x=25, y=200)
    question1 = Label(text="we encode.....", fg="black", bg='#156286', font="Arial 20 bold")
    question1.place(x=25, y=250)
    #question2 = Label(text="for some time ", fg="black", bg='#156286', font="Arial 20 bold")
    #question2.place(x=25, y=300)

    start = Label(fg="#156286", bg='#156286',command=threading.Thread(target=face_encoding).start())


    app.mainloop()



def data_get():
    import Faculty
    encode()

def data():

    for widget in app.winfo_children():
        widget.destroy()
    # Interface Geometry
    app.geometry("1280x800")
    app.resizable(False, False)
    app.config(background='black')

    # Frames
    data_frame = Frame(app, height=1280, width=350, bg="#156286", bd=2, relief=RAISED)
    data_frame.place(x=0, y=0)

    #######################Gif
    file = "giphy.gif"

    info = Image.open(file)

    frames = info.n_frames
    # print(frames)

    # creating list of PhotoImage objects for each frames
    im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

    coun = 0
    anim = None

    def animatio(coun):
        global anim
        im2 = im[coun]

        gif_label.configure(image=im2)
        coun += 1
        if coun == frames:
            coun = 0
        anim = app.after(50, lambda: animatio(coun))

    gif_label = Label(image="")
    gif_label.place(x=550, y=200)

    animatio(coun)
    #Gif Ends############################################

    # Texts
    welcome = Label(text="Fetching your data !! ", fg="white", bg='black', font="Arial 40 bold")
    welcome.place(x=600, y=50)

    question = Label(text="Have some patience ", fg="black", bg='#156286', font="Arial 20 bold")
    question.place(x=25, y=200)
    question1 = Label(text="We are getting you  ", fg="black", bg='#156286', font="Arial 20 bold")
    question1.place(x=25, y=250)
    question2 = Label(text="your data . ", fg="black", bg='#156286', font="Arial 20 bold")
    question2.place(x=25, y=300)

    start = Label(fg="#156286", bg='#156286',command=threading.Thread(target=data_get).start())
    start.place(x=75, y=400)

    app.mainloop()


#Buttons
get_faculty_students_data = Button(app, text="Get Faculty and Students data " , fg = "white"  , height= '2' , bg= "#0e445d" , relief=RAISED ,command=data)
get_faculty_students_data.place(x = 75 , y =325)

one = Label(app, text="1." , fg = "black"  , height= '2' , bg= "#156286"  , font = "Arial 20 bold")
one.place(x = 25, y =310)

enocode_current_data = Button(app, text="Encode the current data  " , fg = "white"  , height= '2' , bg= "#0e445d" , relief=RAISED ,command=encode)
enocode_current_data.place(x = 75 , y =400)

two = Label(app, text="2." , fg = "black"  , height= '2' , bg= "#156286"  , font = "Arial 20 bold")
two.place(x = 25, y =385)

work_with_current_data = Button(app, text="Work with currrent data " , fg = "white"  , height= '2' , bg= "#0e445d" , relief=RAISED ,command=face)
work_with_current_data.place(x = 75 , y =475)

three = Label(app, text="3." , fg = "black"  , height= '2' , bg= "#156286"  , font = "Arial 20 bold")
three.place(x = 25, y =460)

app.mainloop()