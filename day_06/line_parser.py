import numpy as np

INCREASE = TURN_ON = 0
DECREASE = TURN_OFF = 1
INCREASE_BY_TWO = TOGGLE = 2

line_part_to_instruction = {
    'on': TURN_ON,
    'off': TURN_OFF,
    'toggle': TOGGLE,
}


class LineParser:

    def __init__(self, instruction, selector):
        self.instruction = instruction
        self.selector = selector

    def get_instruction(self):
        return self.instruction

    def get_selector(self):
        return self.selector

    @staticmethod
    def parse_line(line):
        line_parts = line.split(' ')
        if line_parts[0] == 'turn':
            line_parts = line_parts[1:]
        instruction = line_part_to_instruction[line_parts[0]]

        start_coords = tuple(int(x) for x in line_parts[1].split(','))
        end_coords = tuple(int(x) + 1 for x in line_parts[3].split(','))

        x_coords = (start_coords[0], end_coords[0])
        y_coords = (start_coords[1], end_coords[1])

        selector = np.ix_(range(*x_coords), range(*y_coords))

        return LineParser(instruction, selector)
