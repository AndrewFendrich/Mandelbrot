# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 14:22:28 2015

@author: User
"""

import pygame
import math,random
import sys
import time
import gradient6 as gradient

pygame.init()

screenWidth = 800
screenHeight = 600
iterations = 16
framecount = 0
NumberOfColors = 64

Coords0 = (-2,1.0,-1,1.0)
Coords1 = (-1.79,-1.74,-0.02,0.02)
Coords2 = (-1.804,-1.800,-0.02, 0.02)
Coords3 = (-1.7864843750000001,-1.785703125,-0.0003125,0.0003125)
interesting = 0.591
Coords4 = (0.24998645125,interesting,-0.5,0.5)
Coords5 = (0.2816,0,28362157666381815,0.018,0.11464)
Coords = Coords0



Colors = gradient.gradient_list((0,0,0),(255,255,255),NumberOfColors)
print("numberofcolors=",len(Colors))
#print("Number of Colors in the Gradient:",len(Colors))
def HexColorRandom():
    R = int(random.randrange(0,256))
    G = int(random.randrange(0,256))
    B = int(random.randrange(0,256))
    return ((R,G,B))
    
def mandel_pixel(c,n = 256):
    z = c   
    length = len(Colors)
#    print("n= (iterations) = :",n)
    for i in range(n):
        a = z * z
        z=a + c
        if a.real  >= 4.:            
            if (i >= length):
                return(Colors[length-1])
#                return(Colors[len(Colors)])
            return(Colors[i])
#    return (HexColorRandom())
    return((0,0,0))
    
screen = pygame.display.set_mode((screenWidth, screenHeight))
screen.fill(HexColorRandom())

def brot(xa,xb,ya,yb,iterations):
    
    grid = pygame.PixelArray(screen)
#    x = screenWidth
#    y = screenHeight
    
#    xa = -2.0; xb = 1.0
#    ya = -1.27; yb = 1.27
    
    xm=[xa + (xb - xa) * kx /x  for kx in range(x)]
    ym=[ya + (yb - ya) * ky /y  for ky in range(y)]
        
    for i in range(screenWidth):
        for j in range(screenHeight):
            grid[i,j] = mandel_pixel(complex(xm[i],ym[j]),iterations)
        if i % 10 == 0:
            pygame.display.flip()
    pygame.display.flip()
    print("xa:",xa,"xb:",xb,"ya:",ya,"yb:",yb)
#    imagename = []
#    imagename.append("xa" + str(xa) + "xb" + str(xb))
#    imagename.append("ya" + str(ya) + "yb" + str(yb))
#    imagename.append("_W" + str(screenWidth) + "_H" + str(screenHeight))
#    imagename.append("_iter" + str(iterations))   
#    fn = "".join(imagename) 
#    imagename = fn.replace(".","-")
#    print(imagename)
#    print(fn)
#    pygame.image.save(screen,"Images!!!\\" +"151202\\"  + str(framecount) + "1ACF_" + imagename + ".bmp")
    
zoom = 0.50
x = screenWidth
y = screenHeight

xa, xb, ya, yb = Coords[0],Coords[1],Coords[2],Coords[3]
    
#xa = -2.0; xb = 1.0
#ya = -1.27; yb = 1.27
#for i in range(32)
brot(xa,xb,ya,yb,iterations) 

def mouseCoordsToComplexCoords(xa,xb,ya,yb):
    mouse = pygame.mouse.get_pos()
    print("mouseXY:",mouse)
    rcoord = (xb-xa)/screenWidth*mouse[0]+xa
    icoord = (yb-ya)/screenHeight*mouse[1]+ya
    return((rcoord,icoord))
    
def moveWindow(xa,xb,ya,yb,newxc,newyc):
    xc = (xa+xb)/2
    yc = (ya+yb)/2
    xshift = newxc - xc
    yshift = newyc - yc
    newxa = xa + xshift
    newya = ya + yshift
    newxb = xb + xshift
    newyb = yb + yshift
    print("xc",xc,"yc",yc,"xshift",xshift,"yshift",yshift)
    return((newxa,newxb,newya,newyb))
    
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousecoords = mouseCoordsToComplexCoords(xa,xb,ya,yb)
            print("mousecoords:",mousecoords)
            complexcoords = moveWindow(xa,xb,ya,yb,mousecoords[0],mousecoords[1])
            print("ComplecCoords:",complexcoords)
            xa = complexcoords[0]
            xb = complexcoords[1]
            ya = complexcoords[2]
            yb = complexcoords[3]
            print("NEWxa",xa,"NEWxb",xb,"NEWya",ya,"NEWyb",yb)
            brot(xa,xb,ya,yb,iterations)
        elif event.type == pygame.KEYDOWN:
            mods = pygame.key.get_mods()
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_KP8:
                iterations = int(iterations *1.125)
                print("Iterations:",iterations)
            elif event.key == pygame.K_KP5:
                iterations = int(iterations *2)    
                print("Iterations:",iterations)
            elif event.key == pygame.K_KP9:
                NumberOfColors = NumberOfColors + 1
                print("NumberOfColors:",NumberOfColors)
                Colors = gradient.gradient_list((0,0,0),(255,255,255),NumberOfColors)
            elif event.key == pygame.K_KP7:
                NumberOfColors = NumberOfColors - 1
                print("NumberOfColors:",NumberOfColors)
                Colors = gradient.gradient_list((0,0,0),(255,255,255),NumberOfColors)
            elif event.key == pygame.K_KP6:
                NumberOfColors = NumberOfColors + 100
                print("NumberOfColors:",NumberOfColors)
                Colors = gradient.gradient_list((0,0,0),(255,255,255),NumberOfColors)
            elif event.key == pygame.K_KP4:
                NumberOfColors = NumberOfColors - 100
                if NumberOfColors <= 0:
                    NumberOfColors = 1
                print("NumberOfColors:",NumberOfColors)
                Colors = gradient.gradient_list((0,0,0),(255,255,255),NumberOfColors)
            elif event.key == pygame.K_KP2:
                iterations = int(iterations *0.500)
                print("Iterations:",iterations)
            elif event.key == pygame.K_KP_PLUS:
#                x0 = (xa+xb)/2
#                y0 = (ya+yb)/2
#                xscale = abs((x0 - xa)*zoom)
#                yscale = abs((y0 - ya)*zoom)
#                xa = xa + xscale
#                xb = xb - xscale
#                ya = ya + yscale
#                yb = yb - yscale
                """   New Attempt At Zoom """
                x0 = (xa+xb)/2
                y0 = (ya+yb)/2
                xscale = abs((x0 - xa)*zoom)
                yscale = abs((y0 - ya)*zoom)
                xa = xa + xscale
                xb = xb - xscale
                ya = ya + yscale
                yb = yb - yscale
                x1 = screenWidth * zoom / 2
                x2 = screenWidth - screenWidth * zoom / 2
                W = x2 - x1
                y1 = screenHeight * zoom / 2
                y2 = screenHeight * zoom / 2
                H = y2 - y1                
                
                crop = pygame.transform.chop(pygame.transform.chop(screen,(0,0,x1,y1)),(x2,y2,screenWidth,screenHeight))
                pygame.transform.scale(crop,(screenWidth,screenHeight),screen)
#                grid = pygame.PixelArray(screen)
#                grid.transform.scale(scree)                
#                brot(xa,xb,ya,yb,iterations)
            elif event.key == pygame.K_KP_MINUS:
                x0 = (xa+xb)/2
                y0 = (ya+yb)/2
                xscale = abs((x0 - xa)*zoom)
                yscale = abs((y0 - ya)*zoom)
                xa = xa - xscale
                xb = xb + xscale
                ya = ya - yscale
                yb = yb + yscale
#                brot(xa,xb,ya,yb,iterations)
            elif event.key == pygame.K_LEFT:
                shift = abs((xb - xa)*0.5)
                print("shift:",shift,"ya:",ya,"yb",yb)
                xa = xa - shift
                xb = xb - shift
#                brot(xa,xb,ya,yb,iterations)
            elif event.key == pygame.K_RIGHT:
                shift = abs((xb - xa)*0.5)
                xa = xa + shift
                xb = xb + shift
#                brot(xa,xb,ya,yb,iterations)
            elif event.key == pygame.K_UP:
                shift = abs((yb - ya)*0.5)
                ya = ya - shift
                yb = yb - shift  
#                brot(xa,xb,ya,yb,iterations)
            elif event.key == pygame.K_DOWN:
                shift = abs((yb - ya)*0.5)
                ya = ya + shift
                yb = yb + shift 
#                brot(xa,xb,ya,yb,iterations)
            framecount = framecount + 1    
            brot(xa,xb,ya,yb,iterations)