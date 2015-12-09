from input_data import input_data

VOWELS = 'aeiou'

BANNED_STRINGS = ['ab', 'cd', 'pq', 'xy']


def has_at_least_three_vowels(line):
    return len([character for character in line if character in VOWELS]) >= 3


def has_at_least_one_duplicate(line):
    return any([character == line[idx + 1] for (idx, character) in enumerate(line[:-1])])


def has_no_banned_substring(line):
    return len([banned_string for banned_string in BANNED_STRINGS if banned_string in line]) == 0


def is_nice_string(line):
    return has_at_least_three_vowels(line) and has_no_banned_substring(line) and has_at_least_one_duplicate(line)


def solution():
    return len([line for line in input_data if is_nice_string(line)])
