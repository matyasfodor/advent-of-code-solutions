from input_data import input_data

from .circuit import Circuit


def solution():
    circuit1 = Circuit.parse_input(input_data)
    value_a = circuit1.get_wire_data('a')
    circuit2 = Circuit.parse_input(input_data)
    circuit2.set_value('b', value_a)
    return circuit2.get_wire_data('a')
