from input_data import input_data
import json


def extract_sum(data):
    counter = 0
    if isinstance(data, dict):
        if 'red' in data.values():
            return 0
        for value in data.values():
            counter += extract_sum(value)
    elif isinstance(data, list):
        for value in data:
            counter += extract_sum(value)
    elif isinstance(data, int):
        counter += data
    elif isinstance(data, basestring):
        pass
    else:
        raise ValueError('Unhandled object type: ' + str(type(data)))

    return counter


def solution():
    data = json.loads(input_data)

    return extract_sum(data)
