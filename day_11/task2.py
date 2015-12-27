from string import ascii_lowercase
from input_data import input_data

ALPHABET_LENGTH = len(ascii_lowercase)


def string_to_int_list(password):
    return [ord(character) - ord('a') for character in password]


def int_list_to_string(password):
    return ''.join([chr(number + ord('a')) for number in password])


def increase_password(password, position=0):
    if position >= len(password):
        raise ValueError('Not good')
    password[-position - 1] += 1
    if password[-position - 1] >= ALPHABET_LENGTH:
        password[-position - 1] %= ALPHABET_LENGTH
        password = increase_password(password, position + 1)

    return password


def contains_sequence(password):
    for index in range(len(password)-2):
        if password[index] + 1 == password[index + 1] and password[index] + 2 == password[index + 2]:
            return True
    return False


BLACKLIST = string_to_int_list('iol')


def does_not_contain_blacklisted_letter(password):
    return not any(character for character in password if character in BLACKLIST)


def has_two_pairs(password):
    for index1 in range(len(password)-2):
        if password[index1] == password[index1 + 1]:
            for index2 in range(index1 + 2, len(password) - 1):
                if password[index2] == password[index2 + 1]:
                    return True
    return False


def meets_requirements(password):
    return contains_sequence(password) and does_not_contain_blacklisted_letter(password) and has_two_pairs(password)


def solution():
    password = string_to_int_list(input_data)
    password = increase_password(password)

    while not meets_requirements(password):
        password = increase_password(password)

    password = increase_password(password)

    while not meets_requirements(password):
        password = increase_password(password)

    return int_list_to_string(password)
