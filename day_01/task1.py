from collections import Counter
from .input_data import input_data


def solution():
    character_count = Counter(input_data)
    return character_count['('] - character_count[')']
