#!/usr/bin/env python3

from typing import List

def parse_game(data: List[int]) -> str:
    result = [0] * 10
    is_valid = True
    len_data = len(data)

    score = 0
    data_i = 0
    for i in range(len(result)):
        if data_i >= len_data:
            is_valid = False
            break
        if data[data_i] == 10:  # strike
            score += 10
            if i == 9:  # laatste
                if data_i+1 >= len_data:
                    is_valid = False
                    break
                score += data[data_i+1]  # enkel bonus
                data_i += 1  # add one extra, so we can check if we have not too many elements
            else:
                if data_i+2 >= len_data:
                    is_valid = False
                    break
                score += data[data_i+1] + data[data_i+2]  # in het midden
            data_i += 1
        else:
            if data_i+1 >= len_data:
                is_valid = False
                break
            frame_score = data[data_i] + data[data_i + 1]
            if frame_score == 10:  # spare
                if data_i+2 >= len_data:
                    is_valid = False
                    break
                frame_score += data[data_i+2]

            score = score + frame_score
            data_i += 2

        result[i] = score

    if not data_i in [len_data-2, len_data-1, len_data]:  # check if not too many
        is_valid = False

    if is_valid:
        return " ".join(map(str, result))
    else:
        return "INVALID"

if __name__ == "__main__":
    number_of_games = int(input())

    for _ in range(number_of_games):
        print(parse_game(list(map(int, input().split(" ")))))

# vim: set ft=python
