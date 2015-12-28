from .grid import BrokenGrid

from input_data import input_data, NUMBER_OF_ITERATIONS


def solution():
    grid = BrokenGrid.parse_grid(input_data)

    for _ in range(NUMBER_OF_ITERATIONS):
        grid = grid.propagate()

    return grid.number_of_lights_on()
