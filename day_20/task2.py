from .input_data import input_data

import numpy as np


NUMBER_OF_PRESENTS_BY_ELF = 50


def solution():
    minimal_number_of_presents = input_data
    houses = np.zeros(minimal_number_of_presents)
    for elf in range(1, minimal_number_of_presents):
        for index in range(1, 51):
            if elf * index < minimal_number_of_presents:
                houses[elf * index] += elf * 11
        if houses[elf] > minimal_number_of_presents:
            return elf
