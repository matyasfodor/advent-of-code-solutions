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
            yield current_char, counter
            current_char = next_char
            counter = 1
    yield current_char, counter
    return


def solution():
    string_number = str(input_data)
    # string_number = '1'
    # number_of_iterations = 5

    for _ in range(number_of_iterations):
        # counter = Counter(string_number)
        # frequencies = counter.most_common()
        # frequencies.sort(key=lambda frequency_item: int(frequency_item[0]), reverse=True)
        compressed_data = [element for element in compressor(string_number)]
        string_number = ''.join([str(element[1]) + element[0] for element in compressed_data])

    return len(string_number)
