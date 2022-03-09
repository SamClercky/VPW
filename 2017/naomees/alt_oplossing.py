import re

allowed = re.compile(r"(?:^du(\w*)du$)|(?:^ba(\w*)ba$)|(?:^di(\w*)di$)|^(du)+$|^(ba)+$|^(di)+$")

def check_sentence(line):
    hasChanged = True
    current_line = line
    while hasChanged:
        hasChanged = False
        for j in range(1, 6+1):
            result = allowed.fullmatch(current_line)
            if result == None:
                break
            group = result.group(j)
            if group == current_line:
                hasChanged = True
                current_line = ""
                continue
            elif group != None:
                hasChanged = True
                current_line = group
                continue
    if len(current_line) == 0:
        return "naomees"
    else:
        return "onzin"


def naomees(test_id, in_data):
    return str(test_id) + " " + " ".join(check_sentence(line.rstrip()) for line in in_data)


if __name__ == "__main__":
    t = int(input())

    for ti in range(1, t+1):
        in_data = [input() for _ in range(5)]
        print(naomees(ti, in_data))
