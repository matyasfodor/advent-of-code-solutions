from input_data import input_data, total_race_time
from reindeer import Reindeer


def solution():
    reindeers = [Reindeer.parse_line(line) for line in input_data]
    return max([reindeer.compute_distance(total_race_time) for reindeer in reindeers])
