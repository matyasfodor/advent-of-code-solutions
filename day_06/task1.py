import numpy as np

from input_data import input_data


def parse_instructions(line):
    line_parts = line.split(' ')
    if line_parts[0] == 'turn':
        line_parts = line_parts[1:]
    instruction = None
    if line_parts[0] == 'on':
        instruction = 1
    elif line_parts[0] == 'off':
        instruction = 2
    elif line_parts[0] == 'toggle':
        instruction = 0
    if instruction is None:
        raise ValueError('instruction does not match {line}'.format(line=line))
    start_coords = tuple(int(x) for x in line_parts[1].split(','))
    end_coords = tuple(int(x) + 1 for x in line_parts[3].split(','))
    return instruction, start_coords, end_coords


def solution():
    grid_mx = np.ones(shape=(1000,1000)) * -1
    for line in input_data:
        instruction, start_coords, end_coords = parse_instructions(line)
        if instruction == 0:
            grid_mx[start_coords[0]: end_coords[0], start_coords[1]: end_coords[1]] *= -1
        elif instruction == 1:
            grid_mx[start_coords[0]: end_coords[0], start_coords[1]: end_coords[1]] = 1
        elif instruction == 2:
            grid_mx[start_coords[0]: end_coords[0], start_coords[1]: end_coords[1]] = -1
        else:
            raise ValueError('Bad line {line}'.format(line=line))
    return np.concatenate(grid_mx).tolist().count(1)
