import cv2, time, json, os.path
import numpy as np
from tkinter import *
import PIL.Image, PIL.ImageTk

global imageBox, working, currentDirection, data
root = Tk()

def clearDataset():
    global data
    with open("data.json", 'w') as f:
        f.write("{ }")
        data = {}

def handleKeyPress(event):
    global currentDirection
    c = repr(event.char)
    currentDirection = c

def handleKeyRelease(event):
    global currentDirection
    currentDirection = ""

def pilotLoop(videoCapture):
    global imageBox, working, currentDirection, data
    s, img = videoCapture.read() #Get still image from webcam
    if s: #Check if we actually got an image
        img = cv2.resize(img, (400, 300)) #Resize image to fit into window
    else: #Webcam image not found
        print("Error resizing images - assertion failed. Webcam probably not connected.")
        working = False
    #Prepare image to be displayed & display image
    showImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    showImage = PIL.Image.fromarray(showImage)
    root.showImage = showImage = PIL.ImageTk.PhotoImage(showImage)
    imageBox.create_image(0, 0, image=showImage, anchor=NW)
    if(not currentDirection == ''): #If the current direction is anything other than empty,
        print(currentDirection)
        #Record the image and the direction
        with open("data.json") as jsonfile:
            data = json.load(jsonfile)
            data[str(img)] = currentDirection
        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile)
        

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
currentDirection = ''
imageBox = Canvas(root, width=400, height=300)
imageBox.bind("<Key>", handleKeyPress)
imageBox.bind("<KeyRelease>", handleKeyRelease)
imageBox.bind("<1>", lambda event: imageBox.focus_set())
imageBox.pack()
startDrivingButton = Button(root, text = "Start driving!", command = initPilot)
startDrivingButton.pack()
clearDatasetButton = Button(root, text = "Clear dataset", command = clearDataset)
clearDatasetButton.pack()
if(not os.path.isfile("data.json")):
    with open("data.json", 'w+') as f:
        f.write("{ }")
        data = {}
mainloop()