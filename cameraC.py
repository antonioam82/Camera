from tkinter import *
from tkinter import messagebox
#from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image, ImageTk
import threading
import time
import os
import glob

if not os.path.exists(os.getcwd()+"\CAMARA_VIDEOS"):
    os.makedirs("CAMARA_VIDEOS")
os.chdir(os.getcwd()+"\CAMARA_VIDEOS")

def future_file():
    name = "output.avi"
    count = 0
    for i in glob.glob('*.avi'):
        if "output" in i:
            count+=1
    if count>0:
        name = "output"+"("+str(count)+")"+".avi"
    return name

class App:
    def __init__(self,font_video=0):
        global name_file
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        name_file = future_file()
        self.out = cv2.VideoWriter(name_file,self.fourcc, 20.0, (640,480))
        self.appName = "camera"
        self.ventana = Tk()
        self.ventana.title(self.appName)
        self.ventana['bg']='black'
        self.font_video=font_video
        self.recording=False
        self.vid=VideoCaptura(self.font_video)#!!!!!!!!!!!!!!!!!!!!!!!!!
        self.label=Label(self.ventana,text=self.appName,font=15,bg='blue',
                         fg='white').pack(side=TOP,fill=BOTH)
        
        self.canvas=Canvas(self.ventana,bg='red',width=self.vid.width,height=self.vid.height)
        self.canvas.pack()
        self.btnScreenshot = Button(self.ventana,text="Screenshot",width=30,bg='goldenrod2',
                    activebackground='red')
        self.btnScreenshot.pack(side=RIGHT)
        self.btnRecord = Button(self.ventana,text='Record',width=30,bg='red',
                                fg='white',command=self.record)
        self.btnRecord.pack(side=LEFT)
        self.visor()
        self.ventana.mainloop()
        
    def captura(self):
        ver,frame=self.vid.get_frame()
        if ver:
            image="IMG-"+time.strftime("%H-%M-%S-%d-%m")+".jpg"
            cv2.imwrite(image,cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
            
    def visor(self):
        ret, frame=self.vid.get_frame()
        #self.real_color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0,0,image=self.photo,anchor=NW)#0,0
            if self.recording == True:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.out.write(frame)
            self.ventana.after(15,self.visor)

    def record(self):
        global name_file
        if self.recording == False:
            self.recording = True
            self.btnRecord.configure(text='Stop')
        else:
            self.recording = False
            self.btnRecord.configure(text='Record')
            name_file = future_file()
            self.out = cv2.VideoWriter(name_file,self.fourcc, 20.0, (640,480))


class VideoCaptura:
    def __init__(self,font_video=0):
        self.vid = cv2.VideoCapture(font_video)
        if not self.vid.isOpened():
            raise ValueError("No se puede usar esta camara")
        self.width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
    def get_frame(self):
        if self.vid.isOpened():
            verif,frame=self.vid.read()
            if verif:
                return(verif,cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return(verif,None)
        else:
            return(verif,None)
        

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
            os.remove(name_file)
        print("OK")

if __name__=="__main__":
    App()
