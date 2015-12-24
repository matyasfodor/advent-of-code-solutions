from input_data import input_data
from itertools import permutations


def parse_line(line):
    split_line = line.split()
    return split_line[0], split_line[2], int(split_line[4])


def get_cities_and_distances():
    cities = set()
    distances = {}

    for line in input_data:
        origin, destination, distance = parse_line(line)
        cities = cities.union((origin, destination))
        distances.setdefault(origin, {})[destination] = distance

    return cities, distances


def unique_cyclic_permutations(iterable):
    for permutation in permutations(iterable[1:]):
        yield (iterable[0],) + permutation


def solution():
    cities, distances = get_cities_and_distances()
    min_distance = float('inf')

    for permutation in unique_cyclic_permutations(list(cities)):
        permutation_distances = []
        number_of_skips = 0
        for origin, destination in zip(permutation, permutation[1:] + (permutation[0],)):
            if origin in distances and destination in distances[origin]:
                permutation_distances.append(distances[origin][destination])
            else:
                number_of_skips += 1

        if number_of_skips > 1:
            continue

        if len(permutation_distances) == len(cities):
            min_distance_for_permutation = sum(permutation_distances) - max(permutation_distances)
        else:
            min_distance_for_permutation = sum([permutation_distance for permutation_distance in permutation_distances if permutation_distance is not None])

        min_distance = min_distance_for_permutation if min_distance_for_permutation < min_distance else min_distance

        print min_distance_for_permutation
        print permutation
        print permutation_distances
        print '#' * 16

    return min_distance
