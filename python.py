from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb


root=Tk()
root.title("Image Steganography")
root.geometry("720x500+150+180")
root.resizable(False, False)
root.configure(bg="#2D2D34")

def openImage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=(("PNG file","*.png"),
                                                                            ("JPG file","*.jpg"),("All file","*.txt")))

    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    label.configure(image=img,width=250,height=250)
    label.image=img

def save():
    secret.save("hidden.png")

def Hide():
    global secret
    message=text1.get(1.0,END)
    secret=lsb.hide(str(filename),message)

def Show():
    clear_message=lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)


#icon
image_icon=PhotoImage(file="logo.jpg")
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="security.png")
Label(root,image=logo,bg="#2D2D34").place(x=180,y=0)

Label(root,text="Hide Secrets", bg="#2D2D34",fg="#B97375",font="arial 25 bold").place(x=250,y=20)

#Left Frame
f=Frame(root,bd=3,bg="#CEB1BE",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

label=Label(f,bg="#CEB1BE")
label.place(x=40,y=10)

#Right Frame
f2=Frame(root,bd=3,width=340,height=280,bg="white",relief=GROOVE)
f2.place(x=360,y=80)

text1=Text(f2,font="Robote 18",bg="#E2DCDE",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(f2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#Third Frame
f3=Frame(root,bd=3,bg="#2D2D34",width=330,height=100,relief=RIDGE)
f3.place(x=10,y=370)

Button(f3,text="Open Image",width=10,height=2,font="arial 14 bold",bg="#B97375",fg="#F1E4E8",command=openImage).place(x=20,y=30)
Button(f3,text="Save Image",width=10,height=2,font="arial 14 bold",bg="#B97375",fg="#F1E4E8",command=save).place(x=180,y=30)
Label(f3,text="Image File",bg="#2D2D34",fg="#F1E4E8").place(x=20,y=5)

#Fourth Frame
f4=Frame(root,bd=3,bg="#2D2D34",width=330,height=100,relief=RIDGE)
f4.place(x=360,y=370)

Button(f4,text="Hide Data",width=10,height=2,font="arial 14 bold",bg="#B97375",fg="#F1E4E8",command=Hide).place(x=20,y=30)
Button(f4,text="Show Data",width=10,height=2,font="arial 14 bold",bg="#B97375",fg="#F1E4E8",command=Show).place(x=180,y=30)
Label(f4,text="Image File",bg="#2D2D34",fg="#F1E4E8").place(x=20,y=5)




























root.mainloop
