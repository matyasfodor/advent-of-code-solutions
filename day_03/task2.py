from collections import Counter

from .coordinate import Coordinate, CHARACTERS_TO_DIRECTIONS
from .input_data import input_data


def generate_positions(input_data):
    santa_coord = Coordinate(0, 0)
    robo_santa_coord = Coordinate(0, 0)
    yield str(santa_coord)

    for index, character in enumerate(input_data):
        direction = CHARACTERS_TO_DIRECTIONS[character]

        if index % 2 == 0:
            santa_coord += direction
            yield str(santa_coord)
        else:
            robo_santa_coord += direction
            yield str(robo_santa_coord)


def solution():
    visited_coordinates = Counter([position for position in generate_positions(input_data)])

    return len(visited_coordinates.most_common())
