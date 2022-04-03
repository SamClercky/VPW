import numpy as np


Raster = []

path = r'voorbeeld.invoer.txt'

H, D = 0,0

top = lambda x,y : Raster[y-1][x] if y > 0 else None
left  = lambda x,y : Raster[y][x-1] if x > 0 else None

bottom = lambda x,y : Raster[y+1][x] if y < H-1 else None
right  = lambda x,y : Raster[y][x+1] if x < D-1 else None

def initer(x,y):
    ltr = Raster[y][x]
    Raster[y][x] = nrs
    
    if ltr == top(x,y):
        initer(x,y-1)
        
    if ltr == left(x,y):
        initer(x-1,y)
        
    if ltr == right(x,y):
        initer(x+1,y)
        
    if ltr == bottom(x,y):
        initer(x,y+1)
        

def pth(N):
    global nrs
    nrs = 0
    for y in range(H):
        for x in range(D):
            if type(Raster[y][x]) == str:
                initer(x,y)
                nrs = nrs + 1
    NRS = [{None} for _ in range(max(max(Raster))+1)]
    for y in range(H):
        for x in range(D):
            b = Raster[y][x]
            NRS[b].add(a if (a:= top(x,y)) is not b else None)
            NRS[b].add(a if (a:= left(x,y)) is not b else None)
            NRS[b].add(a if (a:= right(x,y)) is not b else None)
            NRS[b].add(a if (a:= bottom(x,y)) is not b else None)
    for i,e in enumerate(NRS):
        e.remove(None)
    for y in range(H):
        print(N, end=' ')
        for x in range(D):
            print(len(NRS[Raster[y][x]]), end=' ')
        print('\n')
            

def readFile():
    with open(path) as FT:
        tot = int(next(FT))
        global H, D, Raster
        for i in range(tot):
            D, H = [int(e) for e in next(FT).strip('\n').split(' ')]
            NRS = []
            Raster = []
            for i in range(H):
                Raster.append([])
                Raster[-1].extend(next(FT).strip('\n'))
            pth(i+1)
        
readFile()
