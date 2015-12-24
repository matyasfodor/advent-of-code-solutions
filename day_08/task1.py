def solution():
    escaped_length = 0
    unescaped_length = 0

    with open('day_08/input.txt', 'r') as input_file:
        lines = [raw_line.rstrip() for raw_line in input_file]

        for line in lines:
            escaped_length += len(line)
            unescaped_length += len(eval(line))

    return escaped_length - unescaped_length
