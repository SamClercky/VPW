# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 08:55:30 2022

@author: Fox Srk
"""

DimH = 5
DimD = 5
Raster = [32, 30, 40, 26, 25, 44, 7, 12, 15, 19,10, 8, 5, 7, 57,9, 1, 3, 6, 25,7, 5, 2, 44, 78]
Pos = []

I = lambda x : (x%DimD,x//DimD)
O = lambda x : x[0] + x[1]*DimD

test = 1

path = r'wedstrijd.invoer.txt'



def FindRaster():
    Min_p = Raster.index(min(Raster))
    Pos.append(Min_p)
    
    while(Pos[-1] != -1):
        last_v = Raster[Pos[-1]]
        i = I(Pos[-1])
        Pos.append(-1)
        if(i[0] > 0 and Raster[Pos[-2]-1] > last_v):
            Pos[-1] = Pos[-2]-1
        if(i[0] < DimD-1 and (temp := Raster[Pos[-2]+1]) > last_v and Raster[Pos[-1]]>temp):
            Pos[-1] = Pos[-2]+1
        if(i[1] > 0 and (temp :=Raster[Pos[-2]-DimD]) > last_v and Raster[Pos[-1]]>temp):
            Pos[-1] = Pos[-2]-DimD
        if(i[1] < DimH-1 and (temp := Raster[Pos[-2]+DimD]) > last_v and Raster[Pos[-1]]>temp):
            Pos[-1] = Pos[-2]+DimD
        Raster[Pos[-2]] = 99
    Pos.pop()
    L = 0x41
    prt = [chr(L + Pos.index(e)) if e in Pos else '.' for e in range(DimH * DimD)]
    for y in range(0,DimH):
        print(test , end=' ')
        for x in range(0,DimD):
            print(prt[x + y*DimH], end='')
        print('\n')
    
with open(path) as FT:
    tot = int(next(FT))
    for T in range(tot):
        Raster = []
        Pos = []
        DimD, DimH = [int(e) for e in next(FT).strip('\n').split(' ')]
        for t in range(DimH):
            Raster.extend([int(e) for e in next(FT).strip('\n').split(' ')])
        FindRaster()
        test += 1
    
        
        
    
    
    

    



