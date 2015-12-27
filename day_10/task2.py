from input_data import input_data, number_of_iterations


def compressor(string_data):
    data = list(string_data)
    current_char = data.pop(0)
    counter = 1
    while len(data) > 0:
        next_char = data.pop(0)
        if current_char == next_char:
            counter += 1
        else:
            yield str(counter) + current_char
            current_char = next_char
            counter = 1
    yield str(counter) + current_char
    return


def solution():
    string_number = str(input_data)
    cache = {}
    for _ in range(50):
        print _
        string_number = ''.join([element for element in compressor(string_number, cache)])

    return len(string_number)
