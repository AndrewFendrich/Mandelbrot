# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 23:25:48 2015

@author: User
"""

import pygame

pygame.init()

rectangle = pygame.Rect(50,50,100,100)
print(rectangle)
rectangle.inflate_ip(2,2)
print(rectangle)