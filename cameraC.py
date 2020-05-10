from tkinter import *
from tkinter import messagebox
import cv2
from mhmovie.code import *
import wave
import pyaudio
import numpy as np
from PIL import Image, ImageTk
import threading
import time
import os
#import glob

class CameraApp():

    def __init__(self,font_video=0):

        self.fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        self.name_file = "output.avi"
        self.out = cv2.VideoWriter(self.name_file,self.fourcc, 20.0, (640,480))
        #name_file = future_file()
        self.recording=False
        #self.hours=0
        #self.minuts=0
        #self.seconds=0
        self.appName = "Video Recorder"
        self.root = Tk()
        self.root.title(self.appName)
        self.root['bg']='black'
        self.font_video = font_video
        
        self.label=Label(self.root,text=self.appName,font=15,bg='blue',
                         fg='white').pack(side=TOP,fill=BOTH)
        
        self.canvas=Canvas(self.root,bg='black')
        self.canvas.pack()
        self.btnScreenshot = Button(self.root,text="Screenshot",width=28,bg='green',fg='white',command=self.captura)
        self.btnRecord = Button(self.root,text='Record',width=29,bg='green',fg='white')
        self.btnRecord.pack(side=LEFT)        
        self.btnScreenshot.pack(side=RIGHT)
        self.counter = Label(self.root,text='00:00:00',bg='black',fg='red',width=27,height=2,font=('Arial',11))
        self.counter.pack(side=LEFT)

        self.init_camera()
            
        self.root.mainloop()

    def record_state(self):
        if self.recording == False:
            self.recording = True
        else:
            self.recording = False

    def captura(self):
        ver,frame=self.get_frame()
        if ver:
            image="IMG-"+time.strftime("%H-%M-%S-%d-%m")+".jpg"
            cv2.imwrite(image,cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
        
    def visor(self):
        if self.vid.isOpened():
            ret, frame = self.get_frame()
            if ret:
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.canvas.create_image(0,0,image=self.photo,anchor=NW)
                self.root.after(15,self.visor)

    def init_camera(self):
        self.vid=cv2.VideoCapture(self.font_video)
        if self.vid.isOpened():
            self.width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
            self.canvas.configure(width=self.width,height=self.height)
            self.visor()
        else:
            messagebox.showwarning("CAMARA NO DISPONIBLE","El dispositivo no está activado o disponible")
        
    def get_frame(self):
        if self.vid.isOpened():
            verif,frame=self.vid.read()
            if verif:
                return(verif,cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return(verif,None)
        else:
            return(verif,None)

              
if __name__=="__main__":
    CameraApp()




