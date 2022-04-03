import numpy as np

KEYS = [[1, 2, 7],
[1, 3, 6],
[1, 5, 4],
[2, 6, 4],
[3, 4, 8],
[3, 7, 2],
[4, 5, 7],
[4, 8, 5],
[5, 6, 3],
[6, 8, 9],
[7, 8, 3]]

def vector(shape):
    rt = np.full(shape, 99) - np.identity(shape[0])*99
    X,Y = np.shape(rt)
    update = set()
    for i in range(0,Y):
        for I in KEYS:
            if I[0]-1 == i:
                q = min(I[2],rt[i][I[1]-1])
                rt[i][I[1]-1] = q
                rt[I[1]-1][i] = q
                update.add((I[1]-1,I[0]-1))
            elif I[1]-1 == i:
                q = min(I[2],rt[i][I[0]-1])
                rt[i][I[0]-1] = q
                rt[I[0]-1][i] = q
                update.add((I[0]-1,I[1]-1))
        while len(update) != 0:
            U = update.pop()
            for T in range(0,Y):
                if ( val := rt[T][U[1]] + rt[U[1]][U[0]] ) < rt[T][U[0]]:
                    rt[T][U[0]] = val
                    rt[U[0]][T] = val
                    update.add((U[0],T))
        update.clear()
    return [[sum([min(rt[xx,s],rt[yy,s]) for s in range(0,Y)]) for yy in range(xx,Y)] for xx in range(0,Y)]
                
RT = vector((8,8))
