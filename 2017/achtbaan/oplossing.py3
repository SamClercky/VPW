
world_size = int(500**(1/3))
world = [[[('.', False) for x in range(world_size)] for y in range(world_size)] for z in range(world_size)]

def dft_oplossing(available_structures):
    pass

if __name__ == "__main__":
    N = int(input())

    for n in range(N):
        opdracht = input()
        (aantal, available_structures) = opdracht.strip().split(" ")
        oplossing = dft_oplossing(available_structures.split(""))
        for line in oplossing:
            print(f"{n} {line}")