import cv2, time
import numpy as np
from tkinter import *
import PIL.Image, PIL.ImageTk

global imageBox, working
root = Tk()

def pilotLoop(videoCapture):
    global imageBox, working
    s, img = videoCapture.read() #Get still image from webcam
    if s: #Check if we actually got an image
        showimg = cv2.resize(img, (400, 300)) #Resize image to fit into window
        s, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) #Put threshold on image to make it easier for AI to learn
        img = cv2.resize(img, (80, 60)) #Resize image for dataset
    else: #Webcam image not found
        print("Error resizing images - assertion failed. Webcam probably not connected.")
        working = False
    #Prepare image to be displayed & display image
    showImage = cv2.cvtColor(showimg, cv2.COLOR_BGR2RGB)
    showImage = PIL.Image.fromarray(showImage)
    root.showImage = showImage = PIL.ImageTk.PhotoImage(showImage)
    imageBox.create_image(0, 0, image=showImage, anchor=NW)

def initPilot():
    startDrivingButton.config(state = DISABLED) #Disable button
    print("Starting video stream...")
    cam = cv2.VideoCapture(0) #Create video capture
    print("Done!")
    working = True
    while working:
        #Run through the thingy & update the window
        pilotLoop(cam)
        root.update()
    startDrivingButton.config(state = ENABLED)

#Setup GUI
imageBox = Canvas(root, width=400, height=300)
imageBox.pack()
startDrivingButton = Button(root, text = "Start driving!", command = initPilot)
startDrivingButton.pack()
mainloop()