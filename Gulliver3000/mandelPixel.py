"""

mandelbrot pixel class

"""
#import math

class mandelPixel():
    def __init__(self,coord = (0,0),iter=0):
        self.coordinate = coord
        self.iteration = iter
        self.z = 0        
        
    def iterate(self,limit):   
        for i in range(limit):
            a = self.z * self.z
            self.z = a + self.coordinate
            self.iteration = self.iteration + 1
            print("Iteraion")
            if a.real  >= 4.0:
                print("Escaped")
                break