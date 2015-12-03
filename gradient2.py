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
    for i in range(int(steps/3)):
        gradientList.append((int(Color1[0]+rinterval*i),255,255))
    for i in range(int(steps/3)):
        gradientList.append((Color2[0],int(Color1[1]+ginterval*i),255))
    for i in range(int(steps/3)):
        gradientList.append((Color2[0],Color2[1],int(Color1[2]+binterval*i)))   
    return gradientList
