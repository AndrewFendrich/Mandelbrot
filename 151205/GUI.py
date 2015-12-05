# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 19:33:16 2015

This is intended to be the main script
It will essentially be a client which listens for commmands from another source
that source is intended to be another window

@author: User
"""
import pygame
import random
import time
from multiprocessing.connection import Client
from multiprocessing.connection import Listener
#from array import array

pygame.init()
address = ('localhost', 6000)

def HexColorRandom():
    R = int(random.randrange(0,256))
    G = int(random.randrange(0,256))
    B = int(random.randrange(0,256))
    return ((R,G,B))

screen = pygame.display.set_mode((300,670))
screen.fill(HexColorRandom())


while True:
#    REDRAW = False
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            sys.exit()
    time.sleep(0.25)
    try:    
        with Listener(address, authkey=b'secret password') as listener:
            with listener.accept() as conn:
                print('connection accepted from', listener.last_accepted)
                conn.send("Hello Client!  You owe me money")
    except:
        print("No receivers detected")
    try:
        with Client(address, authkey=b'secret password') as conn:
            message = conn.recv()
            print(message)
    except:
        print("No broadcasters detected")
"""
original Gulliver loop

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
        
"""