def collect_list():
    n = int(input())
    return [int(input()) for _ in range(n)]


def minmax(volgnummer, lijst):
    mini = 9999999999999
    maxi = -9999999999999
    for i in lijst:
        if i < mini:
            mini = i
        if i > maxi:
            maxi = i
    return volgnummer, mini, maxi


if __name__ == "__main__":
    k = int(input())

    for ki in range(1, k+1):
        print(" ".join(map(str, minmax(ki, collect_list()))))

#test