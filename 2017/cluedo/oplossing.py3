
def get_number_of_carts_per_player(p, l, w):
    return ((p-1) + (l-1) + (w-1))//4


def get_heuristics(steps):
    distributions = [{} for _ in range(4)]
    for step in steps:
        p_from = step[0]
        question = step[1]
        p_to = step[2].rstrip()

        if p_to == "X":
            for pi in (pi for pi in range(4) if pi != int(p_from)-1):
                for qi in question:
                    distributions[pi][qi] = -10000
        else:
            p_to = int(p_to)
            for pi in range(4):
                for qi in question:
                    if pi == p_to-1:
                        distributions[pi][qi] = distributions[pi].get(qi, 0) + 3
                    elif pi < p_to-1:
                        distributions[pi][qi] = distributions[pi].get(qi, 0) - 2
                    elif pi > p_to - 1:
                        distributions[pi][qi] = distributions[pi].get(qi, 0) - 1
    return distributions


def reduce_heuristic(heuristics, number_of_carts_per_player):
    result = []
    for i in range(len(heuristics)):
        heuristic = sorted(heuristics[i].items(), key=lambda item: item[1], reverse=True)
        result.append("".join(sorted(h[0] for h in heuristic[:number_of_carts_per_player])))
    return result


if __name__ == "__main__":
    N = int(input())

    for n in range(N):
        p, l, w = list(map(int, input().split(" ")))
        number_of_steps = int(input())
        steps = [input().split(" ") for _ in range(number_of_steps)]
        heuristics = get_heuristics(steps)
        reduced = reduce_heuristic(heuristics, get_number_of_carts_per_player(p, l, w))
        print(f"{n+1} " + " ".join(reduced))
