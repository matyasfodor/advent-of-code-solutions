from input_data import input_data, total_race_time
from reindeer import PropagatingReindeer


def solution():
    reindeers = [PropagatingReindeer.parse_line(line) for line in input_data]

    for _ in range(total_race_time):
        for reindeer in reindeers:
            reindeer.elapse_second()

        max_distance = max([reindeer.distance for reindeer in reindeers])

        for reindeer in reindeers:
            if reindeer.distance == max_distance:
                reindeer.increase_points()

    return max([reindeer.points for reindeer in reindeers])
