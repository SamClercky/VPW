import queue


def print_kaart(kaart):
    for y in range(len(kaart)):
        print(" ".join(kaart[y]))
    print("-----")


def nbs_to_kaart(kaart, nbs, width, height):
    for y in range(height):
        for x in range(width):
            kaart[y][x] = nbs[kaart[y][x]]


def make_unique(kaart, width, height):
    agenda = queue.PriorityQueue(maxsize=width*height)
    agenda.put((kaart[0][0], kaart[0][0] + "0", 0, 0))  # x, y, from_country
    indices = {kaart[0][0]: 1}

    while not agenda.empty():
        to_country, from_country, x, y = agenda.get()
        if len(kaart[y][x]) == 1:  # not yet visited
            curr_name = to_country
            if curr_name == from_country[0]:  # same color, same country
                kaart[y][x] = from_country
                curr_name = from_country
            else:  # we found a new country
                new_index = indices.get(curr_name, 0)
                indices[curr_name] = new_index + 1
                curr_name = curr_name + str(new_index)
                kaart[y][x] = curr_name
            # expand
            if x+1 < width and len(kaart[y][x+1]) == 1:
                agenda.put((kaart[y][x+1], curr_name, x+1, y))
            if x-1 >= 0 and len(kaart[y][x-1]) == 1:
                agenda.put((kaart[y][x-1], curr_name, x-1, y))
            if y+1 < height and len(kaart[y+1][x]) == 1:
                agenda.put((kaart[y+1][x], curr_name, x, y+1))
            if y-1 >= 0 and len(kaart[y-1][x]) == 1:
                agenda.put((kaart[y-1][x], curr_name, x, y-1))
        elif kaart[y][x][0] == from_country[0]:
            if kaart[y][x] > from_country:
                kaart[y][x] = from_country
            elif kaart[y][x] < from_country:  # found better way, backtrack
                curr_name = kaart[y][x]
                if x + 1 < width and kaart[y][x + 1] == from_country:
                    agenda.put((kaart[y][x + 1], curr_name, x + 1, y))
                if x - 1 >= 0 and kaart[y][x - 1] == from_country:
                    agenda.put((kaart[y][x - 1], curr_name, x - 1, y))
                if y + 1 < height and kaart[y + 1][x] == from_country:
                    agenda.put((kaart[y + 1][x], curr_name, x, y + 1))
                if y - 1 >= 0 and kaart[y - 1][x] == from_country:
                    agenda.put((kaart[y - 1][x], curr_name, x, y - 1))


def count_neightbours(kaart, width, height):
    nbs = {}
    for y in range(height):
        for x in range(width):
            curr_country = kaart[y][x]
            curr_nbs = nbs.get(curr_country, {})
            if x-1 >= 0 and kaart[y][x-1] != curr_country:
                adj = kaart[y][x-1]
                curr_nbs[adj] = 1
            if y-1 >= 0 and kaart[y-1][x] != curr_country:
                adj = kaart[y-1][x]
                curr_nbs[adj] = 1
            if x+1 < width and kaart[y][x+1] != curr_country:
                adj = kaart[y][x+1]
                curr_nbs[adj] = 1
            if y+1 < height and kaart[y+1][x] != curr_country:
                adj = kaart[y+1][x]
                curr_nbs[adj] = 1
            nbs[curr_country] = curr_nbs
    return {k: len(v.keys()) for (k, v) in nbs.items()}


if __name__ == "__main__":
    N = int(input())

    for n in range(N):
        width, height = list(map(int, input().rstrip().split(" ")))

        kaart = []
        for h in range(height):
            kaart.append([c for c in input().rstrip()])

        make_unique(kaart, width, height)
        nbs = count_neightbours(kaart, width, height)
        nbs_to_kaart(kaart, nbs, width, height)

        for y in range(height):
            print(n+1, " ".join(map(str, kaart[y])))
