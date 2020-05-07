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
        
        self.hours=0
        self.minuts=0
        self.seconds=0
        self.appName = "Video Recorder"
        self.root = Tk()
        self.root.title(self.appName)
        self.root['bg']='black'
        self.font_video = self.font_video

        self.label=Label(self.root,text=self.appName,font=15,bg='blue',
                         fg='white').pack(side=TOP,fill=BOTH)
        
        self.canvas=Canvas(self.root,bg='black')
        self.canvas.pack()
        self.btnScreenshot = Button(self.root,text="Screenshot",width=28,bg='green',fg='white')
        self.btnRecord = Button(self.root,text='Record',width=29,bg='green',fg='white')
        self.btnRecord.pack(side=LEFT)        
        self.btnScreenshot.pack(side=RIGHT)
        self.counter = Label(self.root,text='00:00:00',bg='black',fg='red',width=27,height=2,font=('Arial',11))
        self.counter.pack(side=LEFT)

        self.root.mainloop()


if __name__=="__main__":
    CameraApp()



