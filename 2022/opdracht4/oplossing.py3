def binsearch(l, e):
    low, high = 0, len(l)
    while high - low > 1:
        pivot = (high + low)//2
        if l[pivot] < e:
            high = pivot
        elif l[pivot] > e:
            low = pivot
        else:
            return pivot
    return -1


if __name__ == "__main__":
    N = int(input())

    for n in range(N):
        ln = int(input())
        if ln == 0:
            print(n+1)
            input()
            continue
        lo = list(map(int, input().rstrip().split(" ")))
        ls = sorted(lo)
        lsol = []
        for e in lo:
            #i = binsearch(ls, e)
            i = 0
            for ii, ei in enumerate(ls):
                if ei == e:
                    i = ii
                    break
            del ls[i]
            lsol.append(i)
        print(n+1, " ".join(map(str, lsol)))
