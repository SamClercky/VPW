allowed = ["ba", "di", "du"]


def check_sentence(line):
    for i in range(0, len(line) // 2, 2):
        word = line[i:i+2]
        if not word in allowed:
            return "onzin"
        last_word = line[-2-i:-i] if i != 0 else line[-2-i:]
        if word != last_word:
            return "onzin"
    return "naomees"


def naomees(test_id, in_data):
    return str(test_id) + " " + " ".join(check_sentence(line.rstrip()) for line in in_data)


if __name__ == "__main__":
    t = int(input())

    for ti in range(1, t+1):
        in_data = [input() for _ in range(5)]
        print(naomees(ti, in_data))