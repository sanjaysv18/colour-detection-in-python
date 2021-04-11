# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 12:22:00 2020

@author: Sevenoaks
"""
#Python project to detect the colour names from an image

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
import pandas as pd
import argparse
from tkinter import filedialog
import tkinter
import tkinter.filedialog

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

img = cv2.imread(root.filename)
red = green = blue = xpos = ypos = 0
index=["color","name","hexval","Red","Green","Blue"]
csv = pd.read_csv('colors.csv', names=index, header=None)

def cname(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"Red"])) + abs(G- int(csv.loc[i,"Green"]))+ abs(B- int(csv.loc[i,"Blue"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"name"]
    return cname


def getcoord(event, x,y,flags,param):
       # print(x,y)
        global blue,green,red,xpos,ypos
        xpos = x
        ypos = y
        blue,green,red = img[y,x]
        blue = int(blue)
        green = int(green)
        red = int(red)
        
       
cv2.namedWindow('Colour Detection')
cv2.setMouseCallback('Colour Detection',getcoord)



while(True):
            cv2.imshow("Colour Detection",img)
           
            cv2.rectangle(img,(3,662), (1359,732), (blue,green,red), -1)
            cv2.rectangle(img,(5,20), (191,31), (0,0,0), -1)
            text="press esc to cancel"
            cv2.putText(img, text,(5,20),2,0.8,(255,255,255),2,cv2.LINE_4)

            text1 ='colour  is:'+ cname(red,green,blue) 
            text2 ='Hex Values are: Red='+ str(red) +  ' Green='+ str(green) +  ' Blue='+ str(blue)

            cv2.putText(img, text1,(392,685),2,0.8,(255,255,255),2,cv2.LINE_4)
            cv2.putText(img, text2,(392,723),2,0.8,(255,255,255),2,cv2.LINE_AA)
        
            if(red+green+blue>=600):
                cv2.putText(img, text1,(392,685),2,0.8,(255,255,255),2,cv2.LINE_4)
                cv2.putText(img, text2,(392,723),2,0.8,(255,255,255),2,cv2.LINE_AA)
        
            if cv2.waitKey(20) & 0xFF ==27:
                break
            
cv2.destroyAllWindows()

