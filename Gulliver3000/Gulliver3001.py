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

iterations = 24


gradient = gradient.linear_gradient([50,15,1],[255,255,199],iterations)


for thing in gradient:
    print(thing)

