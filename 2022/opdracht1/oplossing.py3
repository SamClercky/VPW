def gen_max(inp):
    idx, mx = max(enumerate(inp[2:]), key=lambda i: i[1])
    return idx + 2, mx


def gen_min(inp):
    idx, mn = min(enumerate(inp[2:]), key=lambda i: i[1])
    return idx + 2, mn


if __name__ == "__main__":
    N = int(input())

    for n in range(N):
        inp = list(map(int, input().rstrip().split(" ")))

        split = 0
        imx, mx = gen_max(inp)
        imn, mn = gen_min(inp)
        while mx-mn > inp[0]:
            split += 1

            inp[imx] = mx >> 1
            inp.append((mx & 1) + (mx >> 1))

            imx, mx = gen_max(inp)
            imn, mn = gen_min(inp)

        print(f"{n+1} {split}")
