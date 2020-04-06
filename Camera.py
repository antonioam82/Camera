from tkinter import *
import cv2
import numpy as np
from PIL import Image, ImageTk
import time

def update():
    global photo
    ret, frame = vid.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    photo=ImageTk.PhotoImage(image=Image.fromarray(frame))#!!!!!!!!!!!!!!
    canvas.create_image(0,0,image=photo,anchor=NW)#0,0
    ventana.after(15,update)
    
ventana = Tk()
ventana.title("WebCam")
ventana.resizable(0,0)
ventana['bg']='black'
video_source = 0

vid=cv2.VideoCapture(0)

#ELEMENTOS.
label = Label(ventana,text="CAM",font=15,bg='blue',fg='white')
label.pack(side=TOP,fill=BOTH)
canvas=Canvas(ventana,bg='red')
canvas.pack()
btnScreenshot=Button(ventana,text="Screenshot",width=30,bg='goldenrod2',
                    activebackground='red')
btnScreenshot.pack(anchor=CENTER,expand=True)
update()
ventana.mainloop()


