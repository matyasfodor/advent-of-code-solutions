from collections import Counter

from .coordinate import Coordinate, CHARACTERS_TO_DIRECTIONS
from .input_data import input_data


def generate_positions(input_data):
    current_coordinate = Coordinate(0, 0)
    yield str(current_coordinate)

    for character in input_data:
        direction = CHARACTERS_TO_DIRECTIONS[character]
        current_coordinate += direction
        yield str(current_coordinate)


def solution():
    visited_coordinates = Counter([position for position in generate_positions(input_data)])

    return len(visited_coordinates.most_common())
