import re


def solution():
    escaped_length = 0
    unescaped_length = 0

    with open('day_08/input.txt', 'r') as input_file:
        lines = [raw_line.rstrip() for raw_line in input_file]

        for line in lines:
            unescaped_length += len(line)
            escaped_length += len(re.escape(line)) + 2  # +2 for the starting and trailing quotation marks

    return escaped_length - unescaped_length
