from tkinter import *
import cv2
import numpy as np
from PIL import Image, ImageTk
import time

class App:
    def __init__(self,font_video=0):
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
        self.btnScreenshot = Button(self.ventana,text="PHOTO",width=28,bg='goldenrod2',
                    activebackground='red',command=self.captura)
        self.btnScreenshot.pack(side=RIGHT)
        self.btnVideo = Button(self.ventana,text="VIDEO",width=28,bg='goldenrod2',
                    activebackground='red')
        self.timeLabel = Label(self.ventana,text="0:00:00",bg="black",fg="green",font=('arial',12),width=25)
        self.timeLabel.pack(side=RIGHT)
        self.btnVideo.pack(side=LEFT)
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
            self.ventana.after(15,self.visor)

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
        print("OK")
        if self.vid.isOpened():
            self.vid.release()
                
if __name__=="__main__":
    App()
