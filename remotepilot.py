#import serial
import cv2, time
import numpy as np
from PIL import Image, ImageTk
from tkinter import *

global infoBox
root = Tk()

def pilotLoop(videoCapture):
    global infoBox
    while True:
        s, img = videoCapture.read()
        s, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        if s:
            print("S", s, "IMG", img)
            img = cv2.resize(img, (80, 60))
        else:
            infoBox.insert(END, "Error resizing image: Assertion failed.\n")
            
def initPilot():
    startDrivingButton.config(state = DISABLED)
    infoBox.insert(END, "Connecting to camera and setting up video stream...")
    cam = cv2.VideoCapture(0)
    infoBox.insert(END, " Done.\n")
    pilotLoop(cam)

#Setup GUI
startDrivingButton = Button(root, text = "Start driving!", command = initPilot)
startDrivingButton.pack()
infoBox = Text(root)
infoBox.pack()

mainloop()