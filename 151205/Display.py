# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 14:22:28 2015

@author: User
"""

import pygame
import math,random
import sys, os
import time, datetime
import gradient7 as gradient
import messenger

pygame.init()

screenWidth = 320
screenHeight = 240
iterations = 32
frameCount = 0
NumberOfColors = 128
colorBands = int(screenWidth/NumberOfColors)
color1 = (0,0,0)
color2 = (255,255,255)
Colors = gradient.gradient_list(color1,color2,NumberOfColors,colorBands)
date = time.strftime("%Y%m%d")
folderPath = "Images\\" + str(date + "\\")


###   defining starting coordinates ###
Coords0 = (-2,1.0,-1,1.0)
Coords1 = (-1.79,-1.74,-0.02,0.02)
Coords2 = (-1.804,-1.800,-0.02, 0.02)
Coords3 = (-1.7864843750000001,-1.785703125,-0.0003125,0.0003125)
interesting = 0.591
Coords4 = (0.24998645125,interesting,-0.5,0.5)
Coords5 = (0.2816,0,28362157666381815,0.018,0.11464)

Coords = Coords0

#######################################


def HexColorRandom():
    R = int(random.randrange(0,256))
    G = int(random.randrange(0,256))
    B = int(random.randrange(0,256))
    return ((R,G,B))

screen = pygame.display.set_mode((screenWidth, screenHeight))
screen.fill(HexColorRandom())
    
def mandel_pixel(c,n = 256):
    z = c   
    length = len(Colors)
    for i in range(n):
        a = z * z
        z=a + c
        if a.real  >= 4.:            
            if (i >= length):
                return(Colors[length-1])
            return(Colors[i])
    return((0,0,0))

def create_if_necessary(folderPath):
#    d = os.path.dirname(folderPath)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

def brot(complexCoords,iterations,frameCount):
    xa = complexCoords[0]
    xb = complexCoords[1]
    ya = complexCoords[2]
    yb = complexCoords[3]
    
    grid = pygame.PixelArray(screen)
    
    xm=[xa + (xb - xa) * kx /x  for kx in range(x)]
    ym=[ya + (yb - ya) * ky /y  for ky in range(y)]
        
    for i in range(screenWidth):
        grid[i] = HexColorRandom()
        pygame.display.flip()
        for j in range(screenHeight):
            grid[i,j] = mandel_pixel(complex(xm[i],ym[j]),iterations)
    pygame.display.flip()
    imagename = []
    imagename.append("xa" + str(xa) + "xb" + str(xb))
    imagename.append("ya" + str(ya) + "yb" + str(yb))
    imagename.append("_iter" + str(iterations))    
    fn = "".join(imagename) 
    imagename = fn.replace(".","-")
    create_if_necessary(folderPath)
    pygame.image.save(screen,folderPath + str(frameCount) + "-_xACFx_-" + imagename + ".bmp")

zoom = 0.50
x = screenWidth
y = screenHeight

xa, xb, ya, yb = Coords[0],Coords[1],Coords[2],Coords[3]
    
#xa = -2.0; xb = 1.0
#ya = -1.27; yb = 1.27
#for i in range(32)

brot(Coords,iterations,0) 

def mouseCoordsToComplexCoords(complexCoords):
    xa = complexCoords[0]
    xb = complexCoords[1]
    ya = complexCoords[2]
    yb = complexCoords[3]    

    mouse = pygame.mouse.get_pos()
    real = (xb-xa)/screenWidth*mouse[0]+xa
    imaginary = (yb-ya)/screenHeight*mouse[1]+ya

    print("mouseCoordsToComplexCoords (real,imaginary):",(real,imaginary))    
    return((real,imaginary))
    
def moveWindow(complexCoords,newxc,newyc):
    xa = complexCoords[0]
    xb = complexCoords[1]
    ya = complexCoords[2]
    yb = complexCoords[3]
    
    xc = (xa+xb)/2
    yc = (ya+yb)/2
    xshift = newxc - xc
    yshift = newyc - yc

    newCoords = []    
    newCoords.append(xa + xshift)
    newCoords.append(xb + xshift)
    newCoords.append(ya + yshift)
    newCoords.append(yb + yshift)

    print("moveWindow newCoords:",newCoords)
    return(newCoords)

def zoomIn(complexCoords,scale):
    xa = complexCoords[0]
    xb = complexCoords[1]
    ya = complexCoords[2]
    yb = complexCoords[3]    

    x0 = (xa+xb)/2
    y0 = (ya+yb)/2
    xscale = abs((x0 - xa)*scale)
    yscale = abs((y0 - ya)*scale)

    newCoords = []
    newCoords.append(xa + xscale)
    newCoords.append(xb - xscale)
    newCoords.append(ya + yscale)
    newCoords.append(yb - yscale)

    print("zoomIn newCoords:",newCoords)
    return(newCoords)

def zoomOut(complexCoords,scale):
    xa = complexCoords[0]
    xb = complexCoords[1]
    ya = complexCoords[2]
    yb = complexCoords[3]

    x0 = (xa+xb)/2
    y0 = (ya+yb)/2
    xscale = abs((x0 - xa)*scale)
    yscale = abs((y0 - ya)*scale)

    newCoords = []
    newCoords.append(xa - xscale)
    newCoords.append(xb + xscale)
    newCoords.append(ya - yscale)
    newCoords.append(yb + yscale)
    
    print("zoomOut newCoords:",newCoords)
    return(newCoords)


#from multiprocessing.connection import Client, Listener

#address = ('localhost', 6000)     # family is deduced to be 'AF_INET'


while True:    
    Idle = True
    Redraw = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            Idle = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousecoords = mouseCoordsToComplexCoords(Coords)
            Coords = moveWindow(Coords,mousecoords[0],mousecoords[1])
            Idle = False
   
    if Idle:
        messenger.talk("Idle","broadcast")
    messageIn = messenger.listen()
    if not messageIn:
        print(messageIn)
        Idle = False
###  Create the event 
    print("colorBands:",colorBands,"Iterations:",iterations) 
    REDRAW = False
    if REDRAW == True:
        brot(Coords,iterations,frameCount)
        frameCount = frameCount + 1
        print(Coords)