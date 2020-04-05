from tkinter import *
import cv2
from PIL import Image, ImageTk
import time

ventana = Tk()
ventana.title("WebCam")
ventana.resizable(0,0)
ventana['bg']='black'
video_source = 0

#ELEMENTOS.
label = Label(ventana,text="WEBCAM",font=15,bg='blue',fg='white')
label.pack(side=TOP,fill=BOTH)
canvas=Canvas(ventana,bg='red').pack()

ventana.mainloop()

