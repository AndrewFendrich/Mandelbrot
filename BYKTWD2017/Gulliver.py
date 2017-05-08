# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 14:22:28 2015

@author: User
"""

import pygame
import math,random
import sys, os
import time
import gradient8 as gradient

pygame.init()

screenWidth = 1600
screenHeight = 1000
menuHeight = 90
iterations = 64
framecount = 0
NumberOfColors = 64

# These are a collection of starting coordintaes for the program.  
# The program does not need to begin zoomed all the way 'out'
# You can set the coordinates to any location.  The window coordinates are
# output to the console and if you find interesting locations, set them here
# to collect neat starting locations.
screenHeight = screenHeight - menuHeight
Coords0 = (-2,1.0,-1,1.0)
Coords1 = (-1.79,-1.74,-0.02,0.02)
Coords2 = (-1.804,-1.800,-0.02, 0.02)
Coords3 = (-1.7864843750000001,-1.785703125,-0.0003125,0.0003125)
interesting = 0.591
Coords4 = (0.24998645125,interesting,-0.5,0.5)
Coords5 = (0.2816,0,28362157666381815,0.018,0.11464)


#Here we assign the starting coordinates for the initial image.
Coords = Coords0

Colors = gradient.gradient_list((0,0,0),(255,255,255),NumberOfColors)
print("numberofcolors=",len(Colors))


def HexColorRandom():
    R = int(random.randrange(0,256))
    G = int(random.randrange(0,256))
    B = int(random.randrange(0,256))
    return ((R,G,B))

def RandomColorGradient():
    Color1 = HexColorRandom()
    Color2 = HexColorRandom()
    RandomGradient = gradient.gradient_list(Color1,Color2,NumberOfColors)
    print(RandomGradient)
    return RandomGradient


# mandel_pixel is the heart of the image.  This is the iterative routine
# which performs the calculation for each pixel.  c is the pixels complex
# coordinate and n is maximum number of iterations to attempt.  If the result
# does not 'escape' before reaching n, then the color applied is black.    
def mandel_pixel(c,n = 256):
    z = c 
    a = c
    length = len(Colors)
    for i in range(n):
        a = z * z #standard Mandelbrot
#   Commented out below are a few other interesting expressions which generate
#   interesting pictures.  Use any single line (or multiple? why not?).        
#        a = z * z * z * z #TripleBrot
#        a = z*c
#        a = z*(c-a*c+z) #exploded sides
#        a = 1/(z*z) #KlingonBrot        
        z=a + c
        if a.real  >= 4.0:            
            if (i >= length):
                return((200,200,200))
#                return(Colors[length-1])
#            return(Colors[int((i/n)*(length-1))])
            return((200,200,200))
    return((0,0,0))

# The screen is initialized and the background filled with a random color    
screen = pygame.display.set_mode((screenWidth, screenHeight))
screen.fill(HexColorRandom())

def brot(xa,xb,ya,yb,iterations):
    
    grid = pygame.PixelArray(screen)
   
    xm=[xa + (xb - xa) * kx /x  for kx in range(x)]
    ym=[ya + (yb - ya) * ky /y  for ky in range(y)]

# For every pixel on the screen, calculate the iteration/escape value
# the screen is updated periodically while calculating.
        
    for i in range(screenWidth):
        for j in range(screenHeight):
            grid[i,j] = mandel_pixel(complex(xm[i],ym[j]),iterations)
#   "if i % 15 == 0:"  after each '15th' column the display will be updated.
        if i % 15 == 0:
            pygame.display.flip()
#   Ultimately update the screen when all pixels have been calculated
    pygame.display.flip()

# This section builds a filename for every picture generated.
    print("xa:",xa,"xb:",xb,"ya:",ya,"yb:",yb)
    imagename = []
    imagename.append("xa" + str(xa) + "xb" + str(xb))
    imagename.append("ya" + str(ya) + "yb" + str(yb))
    imagename.append("_W" + str(screenWidth) + "_H" + str(screenHeight))
    imagename.append("_iter" + str(iterations))   
    fn = "".join(imagename) 
    imagename = fn.replace(".","-")
    print(imagename)
    print(fn)
# Here we actually save the screen image
    pygame.image.save(screen,"BYKTWD2017_" + str(framecount) + "_RPi_" + imagename + ".bmp")
    
zoom = 0.50 #the zoom amount when + or - is pressed.
x = screenWidth
y = screenHeight

xa, xb, ya, yb = Coords[0],Coords[1],Coords[2],Coords[3]
    
brot(xa,xb,ya,yb,iterations) #generates the initial image set

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
    
# This is the running code loop.  On any event the picture will recalculate
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
            elif event.key == pygame.K_c:
                Colors = RandomColorGradient()
                print("Random Color Gradient Generated")
            elif event.key == pygame.K_KP8:
                iterations = int(iterations *1.25)
                print("Iterations:",iterations)
            elif event.key == pygame.K_KP5:
                iterations = int(iterations *2)    
                print("Iterations:",iterations)
            elif event.key == pygame.K_KP2:
                iterations = int(iterations *0.500)
                print("Iterations:",iterations)
            elif event.key == pygame.K_KP9:
                NumberOfColors = int(NumberOfColors *1.25)
                print("NumberOfColors:",NumberOfColors)
                Colors = gradient.gradient_list((0,0,0),(255,255,255),NumberOfColors)
            elif event.key == pygame.K_KP6:
                NumberOfColors = int(NumberOfColors *2.0)
                print("NumberOfColors:",NumberOfColors)
                Colors = gradient.gradient_list((0,0,0),(255,255,255),NumberOfColors)
            elif event.key == pygame.K_KP3:
                NumberOfColors = int(NumberOfColors *0.5)
                print("NumberOfColors:",NumberOfColors)
                Colors = gradient.gradient_list((0,0,0),(255,255,255),NumberOfColors)
            elif event.key == pygame.K_KP_PLUS:
                x0 = (xa+xb)/2
                y0 = (ya+yb)/2
                xscale = abs((x0 - xa)*zoom)
                yscale = abs((y0 - ya)*zoom)
                xa = xa + xscale
                xb = xb - xscale
                ya = ya + yscale
                yb = yb - yscale
            elif event.key == pygame.K_KP_MINUS:
                x0 = (xa+xb)/2
                y0 = (ya+yb)/2
                xscale = abs((x0 - xa)*zoom)
                yscale = abs((y0 - ya)*zoom)
                xa = xa - xscale
                xb = xb + xscale
                ya = ya - yscale
                yb = yb + yscale
            elif event.key == pygame.K_LEFT:
                shift = abs((xb - xa)*0.5)
                print("shift:",shift,"ya:",ya,"yb",yb)
                xa = xa - shift
                xb = xb - shift
            elif event.key == pygame.K_RIGHT:
                shift = abs((xb - xa)*0.5)
                xa = xa + shift
                xb = xb + shift
            elif event.key == pygame.K_UP:
                shift = abs((yb - ya)*0.5)
                ya = ya - shift
                yb = yb - shift  
            elif event.key == pygame.K_DOWN:
                shift = abs((yb - ya)*0.5)
                ya = ya + shift
                yb = yb + shift 
            framecount = framecount + 1    
            brot(xa,xb,ya,yb,iterations)
