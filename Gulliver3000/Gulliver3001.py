# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:30:31 2016

@author: User
"""

import pygame
import math,random
import sys
import time
import gradient
import mandelPixel

a = complex(1.1,-1)

Pixel = mandelPixel.mandelPixel(a)

for i in range(30):
    if(Pixel.iterate()):
        break

Grid = mandelPixel.grid(-a,a,4,4)

for i in range(30):
    if(Grid.grid[2][2].iterate()):
        break