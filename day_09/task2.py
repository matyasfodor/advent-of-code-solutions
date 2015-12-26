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
        distances.setdefault(destination, {})[origin] = distance

    return cities, distances


def compute_path_distances(path, distances):
    path_distances = []
    for origin, destination in zip(path, path[1:] + path[0:1]):
        if origin in distances and destination in distances[origin]:
            path_distances.append(distances[origin][destination])
        else:
            return None
    return path_distances


def unique_cyclic_permutations(iterable):
    copy_iterable = iterable.copy()
    first_element = copy_iterable.pop()
    for permutation in permutations(copy_iterable):
        yield (first_element,) + permutation


def solution():
    cities, distances = get_cities_and_distances()
    max_path_distance = -float('inf')

    for permutation in unique_cyclic_permutations(cities):
        path_distances = compute_path_distances(permutation, distances)
        if path_distances is not None:
            path_distance = sum(path_distances) - min(path_distances)
            if path_distance > max_path_distance:
                max_path_distance = path_distance

    return max_path_distance
