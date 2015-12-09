import numpy as np

from input_data import input_data
from line_parser import TURN_ON, TURN_OFF, TOGGLE, LineParser


def solution():
    grid_mx = np.ones(shape=(1000, 1000)) * -1

    for line in input_data:
        line_parser = LineParser.parse_line(line)
        instruction = line_parser.get_instruction()
        selector = line_parser.get_selector()

        if instruction == TURN_ON:
            grid_mx[selector] = 1
        elif instruction == TURN_OFF:
            grid_mx[selector] = -1
        elif instruction == TOGGLE:
            grid_mx[selector] *= -1

    return np.concatenate(grid_mx).tolist().count(1)
