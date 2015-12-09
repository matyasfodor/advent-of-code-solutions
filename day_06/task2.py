import numpy as np

from input_data import input_data
from line_parser import INCREASE, DECREASE, INCREASE_BY_TWO, LineParser


def solution():
    grid_mx = np.zeros(shape=(1000, 1000))

    for line in input_data:
        line_parser = LineParser.parse_line(line)
        instruction = line_parser.get_instruction()
        selector = line_parser.get_selector()

        if instruction == INCREASE:
            grid_mx[selector] += 1
        elif instruction == DECREASE:
            grid_mx[selector] -= 1
            grid_mx[np.where(grid_mx < 0)] = 0
        elif instruction == INCREASE_BY_TWO:
            grid_mx[selector] += 2

    return np.sum(np.concatenate(grid_mx))
