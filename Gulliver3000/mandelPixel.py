"""

mandelbrot pixel class

"""
#import math

class grid():
    def __init__(self,CoordTL,CoordBR,HSize,VSize):
        self.CoordTL = CoordTL
        self.CoordBR = CoordBR
        self.HSize = HSize
        self.VSize = VSize
        xa = self.CoordTL.real
        xb = self.CoordBR.real
        ya = self.CoordTL.imag
        yb = self.CoordBR.imag
        xm=[xa + (xb - xa) * kx /HSize  for kx in range(HSize)]
        ym=[ya + (yb - ya) * ky /VSize  for ky in range(VSize)]
        self.grid = [[mandelPixel(complex(x,y)) for x in range(HSize)] for y in range(VSize)]
#        for i in range(HSize):
#            for j in range(VSize):
#                grid[i,j] = mandelPixel(complex(xm[i],ym[j]))
    
"""        
    xm=[xa + (xb - xa) * kx /x  for kx in range(x)]
    ym=[ya + (yb - ya) * ky /y  for ky in range(y)]
"""    
    
class mandelPixel():
    def __init__(self,coordinate = (0,0),iteration=0):
        self.coordinate = coordinate
        self.iteration = iteration
        self.z = 0        
        
    def iterate(self):   
        self.z = self.z * self.z + self.coordinate
        self.iteration = self.iteration + 1
        if self.z.real >= 4.0:
            print(self.z," Escaped")
            return(True)
        print(self.z)
        return(False)