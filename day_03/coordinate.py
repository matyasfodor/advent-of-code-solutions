class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def _get_as_tuple(self):
        return self.x, self.y

    def __iadd__(self, other):
        return Coordinate(*[sum(element_pair) for element_pair in zip(self._get_as_tuple(), other._get_as_tuple())])

    def __str__(self):
        return '{x}_{y}'.format(x=self.x, y=self.y)

EAST = Coordinate(0, 1)
NORTH = Coordinate(1, 0)
WEST = Coordinate(0, -1)
SOUTH = Coordinate(-1, 0)

CHARACTERS_TO_DIRECTIONS = {
    '>': EAST,
    '^': NORTH,
    '<': WEST,
    'v': SOUTH,
}