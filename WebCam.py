from tkinter import *
import cv2
import numpy as np
from PIL import Image, ImageTk
import time

ventana = Tk()
ventana.title("WebCam")
ventana.resizable(0,0)
ventana['bg']='black'
video_source = 0

vid=cv2.VideoCapture(0)

#ELEMENTOS.
label = Label(ventana,text="WEBCAM",font=15,bg='blue',fg='white')
label.pack(side=TOP,fill=BOTH)
canvas=Canvas(ventana,bg='red').pack()
btnScreenshot=Button(ventana,text="Screenshot",width=30,bg='goldenrod2',
                    activebackground='red')
btnScreenshot.pack(anchor=CENTER,expand=True)

ventana.mainloop()


