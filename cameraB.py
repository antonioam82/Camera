from tkinter import *
from tkinter import messagebox
#from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image, ImageTk
import time

def visor():
    global photo
    try:
        ret, frame = vid.read()
        real_color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(image=Image.fromarray(real_color))
        canvas.create_image(0,0,image=photo,anchor=NW)#0,0
        ventana.after(15,visor)
    except:
        messagebox.showwarning("CAMARA NO DISPONIBLE","La camara solicitada no se encuentra disponoble")

def get_frame():
    if vid.isOpened():
        verif, frame = vid.read()
        if verif:
            return(verif, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        else:
            return(verif, None)
    else:
        return(verif, None)

def captura():
    ver,frame = get_frame()
    if ver:
        image="IMG-"+time.strftime("%H-%M-%S-%d-%m")+".jpg"
        cv2.imwrite(image,cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))

#def guardar_en():
    #global archivoGuardar
    #archivoGuardar=filedialog.asksaveasfilename(initialdir="/",title="Guardar en",defaultextension=".jpg")
    #return archivoGuardar

vid = cv2.VideoCapture(0)

if vid.isOpened():
    ventana = Tk()
    ventana.title("CAMERA")
    ventana['bg']='black'
    ventana.resizable(0,0)
    ima_w = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    ima_h = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    #ELEMENTOS.
    label = Label(ventana,text="CAMRI",font = 15,bg ='blue',fg ='white')
    label.pack(side=TOP,fill=BOTH)
    canvas = Canvas(ventana,bg ='red',width=ima_w,height=ima_h)
    canvas.pack()
    btnScreenshot = Button(ventana,text="Screenshot",width=30,bg='goldenrod2',
                    activebackground='red',command=captura)
    btnScreenshot.pack(anchor=CENTER,expand=True)
    visor()


    ventana.mainloop()
else:
    print("CAMARA NO DISPONIBLE")



