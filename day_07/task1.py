from input_data import input_data

from .circuit import Circuit


def solution():
    # test_input = ['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'NOT x -> h', 'NOT y -> i', ]
    # circuit = Circuit.parse_input(test_input)
    # solutions = {
    #     'd': 72,
    #     'e': 507,
    #     'f': 492,
    #     'g': 114,
    #     'h': 65412,
    #     'i': 65079,
    #     'x': 123,
    #     'y': 456,
    # }
    # for solution_element in solutions.keys():
    #     print solution_element, ' ', circuit.get_wire_data(solution_element), ' ', circuit.get_wire_data(solution_element) == solutions[solution_element]
    return Circuit.parse_input(input_data).get_wire_data('a')
