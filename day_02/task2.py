from .input_data import input_data

from .box import Box


def solution():
    boxes = [Box(*[int(dimension) for dimension in dimension_line.split('x')]) for dimension_line in input_data]
    return sum([box.compute_ribbon_required() for box in boxes])
