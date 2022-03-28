def correct_chain(chain):
    chain_striped = chain.rstrip().split("*")
    pattern = {}
    for part in chain_striped:
        pattern[part] = pattern.get(part, 0) + 1
    main_pattern = max(pattern.items(), key=lambda item: item[1])[0]
    len_main = len(main_pattern)

    new_chain = []
    for i in range(len(chain_striped)):
        if len(chain_striped[i]) == len_main or (len(chain_striped[i]) < len_main and i == 0):  # correct part
            new_chain.append(chain_striped[i])
        else:
            if len(chain_striped[i]) < len_main:  # mistake, to short -> change *
                part_len = 0
                part = []
                while part_len < len_main and i < len(chain_striped):  # accumulate parts into 1
                    part.append(chain_striped[i])
                    part_len += len(chain_striped[i])
                    i += 1
                if part_len > len_main:  # check if not accumulated too much
                    part.pop()
                    i -= 1
                new_part = [c for c in ".".join(part)]
                if len(new_part) > len_main:  # When having too much handle it by seeing it as too big
                    if len(new_part) == 2*len_main+1 or i == len(chain_striped):  # At * if possible
                        new_part[len_main] = "*"
                    else:  # if not, weird edge condition -> place one . to the front
                        new_chain[0] = "." + new_chain[0]
                        new_part.pop()
                new_chain.append("".join(new_part))  # At to new chain
            else:  # mistake, to long -> change .
                part = [c for c in chain_striped[i]]
                if i == 0:
                    part[-len_main-1] = "*"
                else:
                    part[len_main] = "*"
                new_chain.append("".join(part))
                i += 1
            new_chain.extend(chain_striped[i:])  # We found the mistake -> copy all the rest
            break

    return "*".join(new_chain)


if __name__ == "__main__":
    N = int(input())

    for n in range(N):
        chain_len = int(input())
        chain = input()
        print(f"{n+1} " + correct_chain(chain))
