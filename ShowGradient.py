# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:27:40 2015

@author: User
"""


import pygame
import math,random
import sys
import time
import gradient7 as gradient

pygame.init()

screenWidth = 1280
screenHeight = 200
colors = 640
colorBands = 1 + int(screenWidth/colors)


screen = pygame.display.set_mode((screenWidth, screenHeight))
grid = pygame.PixelArray(screen)

#columns = int(1 + (screenWidth / steps))

colorgradient = gradient.gradient_list((0,0,0),(255,255,255),colors,colorBands)

print("colorgradient:",len(colorgradient))
colorgradient.append(gradient.gradient_list((0,0,0),(255,255,255),colors,colorBands))
print("colorgradient:",len(colorgradient))

size = len(colorgradient)
step = int(screenWidth/size)

if step == 0:
    step = 1
for i in range(screenWidth):
    print("colors=",size,"index=",i,"Indexed Color::")
    print(colorgradient[i])
    grid[i] = colorgradient[i]
pygame.display.flip()
pygame.image.save(screen,"Images!!!\gradient.bmp")
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            mods = pygame.key.get_mods()
            if event.key == pygame.K_ESCAPE:
                sys.exit()