from md5 import md5

from input_data import input_data


def solution():
    for index in range(0, 10000000):
        m = md5()
        m.update(input_data + str(index))
        if m.hexdigest().startswith('000000'):
            return index
