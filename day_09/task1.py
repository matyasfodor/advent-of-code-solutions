from heapq import heappush, heappop
from input_data import input_data


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


def compute_distances(visited, distances):
    distance = 0
    for origin, destination in zip(visited, visited[1:]):
        if origin in distances and destination in distances[origin]:
            distance += distances[origin][destination]
        else:
            return None
    return distance


def get_start_and_stop_cities(distances):
    start_city = None
    stop_city = None

    sources = set(distances.keys())
    targets = set([target for source in distances.values() for target in source.keys()])
    only_sources = sources - targets

    if len(only_sources) == 1:
        start_city = list(only_sources)[0]

    only_targets = targets - sources

    if len(only_targets) == 1:
        stop_city = list(only_targets)[0]

    return start_city, stop_city


def solution():
    cities, distances = get_cities_and_distances()
    start_city, stop_city = get_start_and_stop_cities(distances)
    print start_city, stop_city

    city_distances = {city: float('inf') for city in cities}
    city_distances[start_city] = 0
    fringe = [start_city]

    while len(fringe) > 0:
        actual = heappop(fringe)

        if actual not in distances:
            continue

        neighbours = distances[actual].keys()
        for neighbour in neighbours:
            neighbour_absolute_distance = city_distances[actual] + distances[actual][neighbour]
            if neighbour_absolute_distance < city_distances[neighbour]:
                city_distances[neighbour] = neighbour_absolute_distance
                heappush(fringe, neighbour)

    return city_distances[stop_city]
