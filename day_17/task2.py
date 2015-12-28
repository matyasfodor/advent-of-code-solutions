from .utils import get_variations
from input_data import input_data, volume


def solution():
    frequencies = {}
    for variation in get_variations(volume, input_data):
        frequencies.setdefault(len(variation), 0)
        frequencies[len(variation)] += 1

    return frequencies[min(frequencies.keys())]
