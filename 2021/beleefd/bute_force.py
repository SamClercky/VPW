# relly naive: do not use, except for dummy data
if __name__ == "__main__":
    for i in range(21):
        for j in range(1, i):
            for k in range(j, i):
                s = sum(range(j, k))
                if s == i:
                    print(f"{i} = {j} + ... + {k-1}")
