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


def fist_f(start, target, distances, city_distances, visited):
    visited.add(start)
    if start not in distances:
        print 'YAAAAY\t', start
        return

    for neighbour in distances[start].keys():
        if neighbour not in visited:
            absolute_distance = city_distances[start] + distances[start][neighbour]
            if neighbour == target:
                if len(visited) == len(city_distances) - 1:
                    yield absolute_distance
            elif absolute_distance < city_distances[neighbour]:
                city_distances[neighbour] = absolute_distance
                for solution_ in fist_f(neighbour, target, distances, city_distances.copy(), visited.copy()):
                    yield solution_
    return


def solution():
    cities, distances = get_cities_and_distances()
    start_city, stop_city = get_start_and_stop_cities(distances)
    print start_city, stop_city
    city_distances = {city: float('inf') for city in cities}
    city_distances[start_city] = 0
    return min(fist_f(start_city, stop_city, distances, city_distances.copy(), set()))
