from tkinter import *
import cv2
import numpy as np
from PIL import Image, ImageTk
import time

def visor():
    global photo
    ret, frame = vid.read()
    real_color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    photo = ImageTk.PhotoImage(image=Image.fromarray(real_color))
    canvas.create_image(0,0,image=photo,anchor=NW)#0,0
    ventana.after(15,visor)
    
ventana = Tk()
ventana.title("Camri")
ventana.resizable(0,0)
ventana['bg']='black'

vid = cv2.VideoCapture(0)
ima_w = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
ima_h = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

#ELEMENTOS.
label = Label(ventana,text="CAM",font = 15,bg ='blue',fg ='white')
label.pack(side=TOP,fill=BOTH)
canvas = Canvas(ventana,bg ='red',width = ima_w,height = ima_h)
canvas.pack()
btnScreenshot = Button(ventana,text = "Screenshot",width = 30,bg ='goldenrod2',
                    activebackground='red')
btnScreenshot.pack(anchor = CENTER,expand = True)
visor()
ventana.mainloop()


