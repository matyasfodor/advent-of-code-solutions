from input_data import input_data

from .circuit import Circuit


def solution():
    return Circuit.parse_input(input_data).get_wire_data('a')
