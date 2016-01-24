# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 14:22:28 2015

@author: User
"""

import pygame
import math,random
import sys
import time
import gradient7 as gradient

pygame.init()

screenWidth = 320
screenHeight = 240
iterations = 64
frameCount = 0
NumberOfColors = 64
colorBands = int(screenWidth/NumberOfColors)
color1 = (0,0,0)
color2 = (255,255,255)
Colors = gradient.gradient_list(color1,color2,NumberOfColors,colorBands)
WalksLoaded = False
#Walks = "0"

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

def imageWalks(WalksLoaded):
#    Walks = "0"
    if WalksLoaded:
        return(Walks)
    else:
        f = open('walks.txt','r')
        print(f)
        Walks = f
        print(Walks)
        Walks = f.readline()
        print("readline:"+Walks)
        f.close()
        f = open('walks.txt','w')
        Walks = str(int(Walks) + 1)
        print("newWalks:" + Walks)
        f.write(Walks)
        f.close()
        WalksLoaded = True
    return(Walks)
    
Walks = ""    
Walks = imageWalks(WalksLoaded)
    
def imageSave():
    pygame.image.save(screen,"Images\\"+ "Walk"+ walks  + "Frame" + str(frameCount) + "ACF" + imagename + ".bmp")
    

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
#        if i % 10 == 0:
#            pygame.display.flip()
    pygame.display.flip()
#    print("xa:",xa,"xb:",xb,"ya:",ya,"yb:",yb)
    imageCenterX = str((xa + xb)/2)
    imageCenterY = str((ya + yb)/2)
    imagename = []
#    imagename.append(Walks)
    imagename.append("cX" + imageCenterX + "cY" + imageCenterY)
    imagename.append("I" + str(iterations))
    imagename.append("H" + str(screenHeight))
    imagename.append("W" + str(screenWidth))
    fn = "".join(imagename) 
    imagename = fn.replace(".","-")

    pygame.image.save(screen,"Images\\"+ "Walk"+ Walks  + "Frame" + str(frameCount) + "ACF" + imagename + ".bmp")

zoom = 0.50
x = screenWidth
y = screenHeight

xa, xb, ya, yb = Coords[0],Coords[1],Coords[2],Coords[3]
    
#xa = -2.0; xb = 1.0
#ya = -1.27; yb = 1.27
#for i in range(32)

#brot(Coords,iterations) 

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

while True:    
    REDRAW = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousecoords = mouseCoordsToComplexCoords(Coords)
            Coords = moveWindow(Coords,mousecoords[0],mousecoords[1])
        elif event.type == pygame.KEYDOWN:
            mods = pygame.key.get_mods()
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_RETURN:
                REDRAW = True
            elif event.key == pygame.K_KP8:
                iterations = int(iterations *1.125)
            elif event.key == pygame.K_KP5:
                iterations = int(iterations *10)    
            elif event.key == pygame.K_KP2:
                iterations = int(iterations/3) 
            elif event.key == pygame.K_KP9:
                Coords = zoomIn(Coords,0.125)
            elif event.key == pygame.K_KP6:
                Coords = zoomIn(Coords,0.90)
            elif event.key == pygame.K_KP3:
                Coords = zoomOut(Coords,1/3)
            elif event.key == pygame.K_KP7:
                colorBands = colorBands +1
                Colors = gradient.gradient_list(color1,color2,NumberOfColors,colorBands)
            elif event.key == pygame.K_KP4:
                colorBands = colorBands *10
                Colors = gradient.gradient_list(color1,color2,NumberOfColors,colorBands)
            elif event.key == pygame.K_KP1:
                colorBands = int(colorBands /10)
                if colorBands <= 1:
                    colorBands = 1    
                Colors = gradient.gradient_list(color1,color2,NumberOfColors,colorBands)           
            if iterations <= 1:
                iterations = 1 
            print("colorBands:",colorBands,"Iterations:",iterations) 
    if REDRAW == True:
        brot(Coords,iterations,frameCount)
        frameCount = frameCount + 1
        print(Coords)