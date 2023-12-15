from AdventOfCode.support import support
import numpy as np
import itertools


class Galaxy:
    def __init__(self, filename, expansion=2):
        self.file_input = np.array(support.read_input(filename, flavor="str_grid"))
        self.row_empty = ["#" not in x for x in self.file_input]
        self.col_empty = ["#" not in x for x in self.file_input.T]
        self.galaxies = np.where(self.file_input == "#")
        self.galaxies = list(zip(self.galaxies[0], self.galaxies[1]))

        # Expand
        for index, item in enumerate(self.galaxies):
            y, x = item
            y += sum(self.row_empty[:y]) * (expansion - 1)
            x += sum(self.col_empty[:x]) * (expansion - 1)
            self.galaxies[index] = (y, x)

        self.pairs = list(itertools.combinations(self.galaxies, 2))
        self.distances = [self.cartesian_dist(x[0], x[1]) for x in self.pairs]
        self.sum = sum(self.distances)

    def cartesian_dist(self, loc1: tuple, loc2: tuple):
        return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])


filename = r"year_2023/tests/test_inputs/11_test_input.txt"
m = Galaxy(filename, expansion=2)
