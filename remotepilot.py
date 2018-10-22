#import serial
import urllib, cv2, time
import numpy as np
from tkinter import *

root = Tk()

global ipEntryField, portEntryField, infoBox

def pilotLoop(ip, port):
    imgURL = "http://" + ip + ":8080/shot.jpg"
    while True:
        with urllib.request.urlopen(imgURL) as url:
            img = url #Read image from phone
        #Decode image
        imgNp = np.array(bytearray(img.read()),dtype=np.uint8)
        img = cv2.imdecode(imgNp,-1)
        #Convert image to 80x60 B/W to make it easier to process
        img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        img = cv2.resize(img, (80, 60))
        


def initPilot():
    global ipEntryField, portEntryField, infoBox
    startDrivingButton.config(state = DISABLED)
    infoBox.insert(END, "Connecting to controller...")
    '''ser = serial.Serial(portEntryField.get(), 9600, timeout = 0, parity = serial.PARITY_EVEN, rtscts = 1)
    ser.write(b'test')
    if(ser.read() == 'g'):
        infoBox.insert(END, "Connected successfully.")
        pilotLoop(ipEntryField.get(), int(portEntryField.get()))
    else:
        infoBox.insert(END, "Connection error. Check serial port and controller version.")
        startDrivingButton.config(state = ENABLED)'''
    infoBox.insert(END, "Connected successfully.")
    #pilotLoop(ipEntryField.get(), int(portEntryField.get()))
    pilotLoop(ipEntryField.get(), 6969)

#Setup GUI
ipEntryLabel = Label(root, text = "IP of camera")
ipEntryLabel.pack()
ipEntryField = Entry(root)
ipEntryField.pack()
portEntryLabel = Label(root, text = "Serial port")
portEntryLabel.pack()
startDrivingButton = Button(root, text = "Start driving!", command = initPilot)
startDrivingButton.pack()
infoBox = Text(root)
infoBox.pack()

mainloop()