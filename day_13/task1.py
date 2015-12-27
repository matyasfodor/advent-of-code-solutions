from input_data import input_data
from itertools import permutations

sign_dict = {
    'lose': -1,
    'gain': 1,
}


def parse_line(line):
    split_line = line.replace('.', '').split()
    parson_a = split_line[0]
    person_b = split_line[-1]
    points = sign_dict[split_line[2]] * int(split_line[3])

    return parson_a, person_b, points


def get_matrix():
    matrix = {}
    for line in input_data:
        person_a, person_b, points = parse_line(line)
        matrix.setdefault(person_a, {})[person_b] = points
    return matrix


def unique_cyclic_permutations(iterable):
    copy_iterable = iterable[:]
    first_element = copy_iterable.pop()
    for permutation in permutations(copy_iterable):
        yield (first_element,) + permutation


def get_happiness(seating_order, matrix):
    happiness = 0
    for person_a, person_b in zip(seating_order, seating_order[1:] + seating_order[0:1]):
        happiness += matrix[person_a][person_b] + matrix[person_b][person_a]
    return happiness


def solution():
    matrix = get_matrix()
    persons = matrix.keys()
    max_happiness = -float('inf')
    for permutation in unique_cyclic_permutations(persons):
        happiness = get_happiness(permutation, matrix)
        if happiness > max_happiness:
            max_happiness = happiness
    return max_happiness
