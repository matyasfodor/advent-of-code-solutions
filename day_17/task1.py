from .utils import get_variations
from input_data import input_data, volume


def solution():
    return len([_ for _ in get_variations(volume, input_data)])
