class Reindeer(object):
    def __init__(self, name, speed, travel_time, rest_time):
        self.name = name
        self.speed = speed
        self.travel_time = travel_time
        self.rest_time = rest_time
        self.cycle_time = travel_time + rest_time

    def compute_distance(self, seconds):
        full_cycles = seconds / self.cycle_time
        additional_time = seconds % self.cycle_time
        return self.speed * (full_cycles * self.travel_time + min(self.travel_time, additional_time))

    @classmethod
    def parse_line(cls, line):
        split_line = line.split()

        return cls(split_line[0], int(split_line[3]), int(split_line[6]), int(split_line[13]))


class PropagatingReindeer(Reindeer):
    def __init__(self, *args):
        super(PropagatingReindeer, self).__init__(*args)
        self.distance = 0
        self.current_time = 0
        self.points = 0

    def elapse_second(self):
        self.current_time += 1
        self.distance = self.compute_distance(self.current_time)

    def increase_points(self):
        self.points += 1
