#def gradient_list((R1,G1,B1),(R2,G2,B2),steps):
#import sys,os

def gradient_list(Color1,Color2,steps):  
    gradientList = []
    
    
    if Color2[0] > Color1[0]:
        rinterval = (Color2[0]-Color1[0])/steps*3
    else:
        rinterval = (Color1[0]-Color2[0])/steps*3
    if Color2[1] > Color1[1]:
        ginterval = (Color2[1]-Color1[1])/steps*3
    else:
        ginterval = (Color1[1]-Color2[1])/steps*3
    if Color2[2] > Color1[2]:
        binterval = (Color2[2]-Color1[2])/steps*3        
    else:
        binterval = (Color1[2]-Color2[2])/steps*3

### Need to make up the difference between the loops and the total number
### of colors to be created "steps"
    redsteps = 1 + int(steps/3)
    greensteps = int(steps/3)
    bluesteps = int(steps/3)

    for i in range(redsteps):
        rc1 = int(Color1[0] +rinterval)
        gradientList.append(((rc1*i,0,0)))
    for i in range(greensteps):
        gc1 = int(Color1[1] +ginterval)
        gradientList.append(((125-(int(125*(i+1)/greensteps)),gc1*i,0)))
    for i in range(bluesteps):
        bc1 = int(Color1[2] +binterval)
        gradientList.append((0,125-(int(125*(i+1)/bluesteps)),bc1*i))
        
    missingcolors = steps - len(gradientList)
    for i in range(missingcolors):
        gradientList.append((255,200,60))
   
    return gradientList
