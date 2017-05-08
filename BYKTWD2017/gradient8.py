#def gradient_list((R1,G1,B1),(R2,G2,B2),steps):
#import sys,os

def gradient_list(Color1,Color2,steps):  
    gradientList = []
    
    
    rinterval = (Color2[0]-Color1[0])/steps*3
    ginterval = (Color2[1]-Color1[1])/steps*3
    binterval = (Color2[2]-Color1[2])/steps*3        

### Need to make up the difference between the loops and the total number
### of colors to be created "steps"
    redsteps = 1 + int(steps/3)
    greensteps = int(steps/3)
    bluesteps = int(steps/3)

    for i in range(redsteps):
        rc1 = int(Color1[0] +rinterval*i)
        gradientList.append(((rc1,0,0)))
    for i in range(greensteps):
        gc1 = int(Color1[1] +ginterval*i)
        gradientList.append(((125-(int(125*(i+1)/greensteps)),gc1,0)))
    for i in range(bluesteps):
        bc1 = int(Color1[2] +binterval*i)
        gradientList.append((0,125-(int(125*(i+1)/bluesteps)),bc1))
        
    missingcolors = steps - len(gradientList)
    for i in range(missingcolors):
        gradientList.append((255,200,60))
   
    return gradientList
