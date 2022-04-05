def transform(case):
    idx, mn = min(enumerate(case), key=lambda c: c[1])
    if case[idx - 1] == mn:
        for _ in range(len(case)):
            idx -= 1
            if case[idx] != mn:
                idx += 1
                break
    idx = (idx + len(case)) % len(case)
    step = 1 if case[(idx + 1) % len(case)] <= case[idx - 1] else -1
    return [case[(idx + step*i + len(case)) % len(case)] for i in range(len(case))]


def solve(cases):
    counts = {}
    for case in cases:
        t_case = transform(case)
        t_case = " ".join(map(str, t_case))
        if counts.get(t_case, None) is not None:
            yield " ".join(map(str, case))
        elif counts.get(t_case[::-1], None) is not None:
            yield " ".join(map(str, case))
        else:
            counts[t_case] = 1


if __name__ == "__main__":
    N = int(input().rstrip())

    for n in range(N):
        cases = []
        for _ in range(int(input())):
            cases.append(list(map(int, input().rstrip().split(" "))))

        sol = list(solve(cases))
        if len(sol) == 0:
            print(f"{n+1} geen duplicaten")
        else:
            for line in sol:
                print(f"{n+1} {line} kwam eerder voor")
