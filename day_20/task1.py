from input_data import input_data


def get_factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def solution():
    minimum_number_of_presents_divided = input_data / 10
    for house_number in range(1, minimum_number_of_presents_divided):
        factors = get_factors(house_number)
        if sum(factors) >= minimum_number_of_presents_divided:
            return house_number
