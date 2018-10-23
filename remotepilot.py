#import serial
import cv2, time
import numpy as np
from tkinter import *
import PIL.Image, PIL.ImageTk

global infoBox, imageBox
root = Tk()

def pilotLoop(videoCapture):
    global infoBox, imageBox
    s, img = videoCapture.read()
    if s:
        showimg = cv2.resize(img, (400, 300))
        s, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        img = cv2.resize(img, (80, 60))
    else:
        print("Error resizing images - assertion failed. Webcam probably not connected.")
    showImage = cv2.cvtColor(showimg, cv2.COLOR_BGR2RGB)
    showImage = PIL.Image.fromarray(showImage)
    root.showImage = showImage = PIL.ImageTk.PhotoImage(showImage)
    imageBox.create_image(0, 0, image=showImage, anchor=NW)

def initPilot():
    startDrivingButton.config(state = DISABLED)
    print("Connecting to camera and starting video stream...")
    cam = cv2.VideoCapture(0)
    print("Done!")
    while True:
        pilotLoop(cam)
        root.update()

#Setup GUI
imageBox = Canvas(root, width=400, height=300)
imageBox.pack()
startDrivingButton = Button(root, text = "Start driving!", command = initPilot)
startDrivingButton.pack()
mainloop()