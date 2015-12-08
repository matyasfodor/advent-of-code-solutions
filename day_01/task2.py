from input_data import input_data


def solution():
    floor = 0
    for index in range(len(input_data)):
        floor += 1 if input_data[index] == '(' else -1
        if floor < 0:
            return index + 1
