#def gradient_list((R1,G1,B1),(R2,G2,B2),steps):
#import sys,os

def gradient_list(Color1,Color2,steps):  
    gradientList = []
    
    
    if Color2[0] > Color1[0]:
        rinterval = (Color2[0]-Color1[0])/steps*6
    else:
        rinterval = (Color1[0]-Color2[0])/steps*6
    if Color2[1] > Color1[1]:
        ginterval = (Color2[1]-Color1[1])/steps*6
    else:
        ginterval = (Color1[1]-Color2[1])/steps*6
    if Color2[2] > Color1[2]:
        binterval = (Color2[2]-Color1[2])/steps*6        
    else:
        binterval = (Color1[2]-Color2[2])/steps*6


    for i in range(1 + int(steps/6)):
        rc1 = int(Color1[0] +rinterval)
        gradientList.append(((rc1*i,0,0)))
    for i in range(1 + int(steps/6)):
        rc2 = 255 - int(rinterval * i)
        gradientList.append((rc2,rc2,rc2))

    for i in range(1 + int(steps/6)):
        gc1 = int(Color1[1] +ginterval)
        gradientList.append((0,gc1*i,0))
    for i in range(1 + int(steps/6)):
        gc2 = 255 - int(ginterval * i)
        gradientList.append((gc2,gc2,gc2))
    
    for i in range(1 + int(steps/6)):
        bc1 = int(Color1[2] +binterval)
        gradientList.append((0,0,bc1*i))
    for i in range(1 + int(steps/6)):
        bc2 = 255 - int(binterval * i)
        gradientList.append((bc2,bc2,bc2))
       
   
    return gradientList
