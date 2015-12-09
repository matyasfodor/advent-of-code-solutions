from input_data import input_data

VOWELS = 'aeiou'

BANNED_STRINGS = ['ab', 'cd', 'pq', 'xy']


def has_a_pair_of_duplicates(line):
    found = False
    for first_idx in range(len(line) - 1):
        for second_idx in range(first_idx + 2, len(line) - 1):
            if line[first_idx: first_idx + 2] == line[second_idx: second_idx + 2]:
                found = True
    return found


def has_pair_one_letter_between(line):
    return any([character == line[idx + 2] for (idx, character) in enumerate(line[:-2])])


def is_nice_string(line):
    return has_a_pair_of_duplicates(line) and has_pair_one_letter_between(line)


def solution():
    return len([line for line in input_data if is_nice_string(line)])
