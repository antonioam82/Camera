from tkinter import *
import cv2
from PIL import Image, ImageTk
import time

ventana = Tk()
ventana.title("WebCam")
ventana.resizable(0,0)
ventana['bg']='black'
video_source = 0

ventana.mainloop()
