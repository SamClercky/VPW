import math


def get_r(haters):
    unique = {}
    for comb in haters:
        for pers in comb:
            unique[pers] = 1
    return len(unique.keys())


def solve(n, c, h, haters):

    if h == 0:
        return math.ceil(n / c)
    if n == h:
        return n
    if n > c:
        return math.ceil(n / c)

    r = get_r(haters)
    if r == h:
        return r

    return math.ceil(n / c) + 1 + (1 if h > 6 else 0)


if __name__ == "__main__":
    N = int(input())

    for ni in range(N):
        n, c, h = list(map(int, input().rstrip().split(" ")))
        haters = []
        for _ in range(h):
            haters.append(input().rstrip().split(" "))

        sol = solve(n, c, h, haters)
        print(f"{ni+1} {sol}")
