import numpy as np

from .consts import parser_dict


class Grid(object):
    def __init__(self, grid):
        self.grid = grid
        self.max_x, self.max_y = grid.shape

    def is_on(self, x, y):
        return self.grid[x, y] == 1

    def set(self, x, y, value):
        self.grid[x, y] = value

    def propagate(self):
        new_grid = self.__class__(np.copy(self.grid))
        for x in range(new_grid.max_x):
            for y in range(new_grid.max_y):
                number_of_neighbours_on = self.get_number_of_neighbours_on(x, y)
                if self.is_on(x, y):
                    if number_of_neighbours_on in [2, 3]:
                        new_grid.set(x, y, 1)
                    else:
                        new_grid.set(x, y, 0)
                if not self.is_on(x, y) and number_of_neighbours_on == 3:
                    new_grid.set(x, y, 1)
        return new_grid

    def get_number_of_neighbours_on(self, x, y):
        counter = 0
        for i in range(max(0, x - 1), min(self.max_x, x + 2)):
            for j in range(max(0, y - 1), min(self.max_y, y + 2)):
                if i == x and j == y:
                    continue
                if self.is_on(i, j):
                    counter += 1
        return counter

    def number_of_lights_on(self):
        return np.sum(self.grid)

    @classmethod
    def parse_grid(cls, grid_input):
        return cls(np.array([[parser_dict[character] for character in line] for line in grid_input]))


class BrokenGrid(Grid):
    def __init__(self, *args):
        super(BrokenGrid, self).__init__(*args)

    def propagate(self):
        new_grid = super(BrokenGrid, self).propagate()

        new_grid.set(0, 0, 1)
        new_grid.set(new_grid.max_x - 1, 0, 1)
        new_grid.set(0, new_grid.max_y - 1, 1)
        new_grid.set(new_grid.max_x - 1, new_grid.max_y - 1, 1)

        return new_grid
