from AdventOfCode.support import support
import itertools
import numpy as np


class ClassName:
    def __init__(self, filename, part2=False):
        self.file_input = support.read_input(filename, flavor="split", split_char=" ")

        h_range, v_range = self.find_grid_extents()
        self.grid = np.zeros(
            [v_range[1] - v_range[0] + 3, h_range[1] - h_range[0] + 3], dtype=int
        )
        self.pos = (v_range[0] * -1 + 1, h_range[0] * -1 + 1)
        self.tag_nodes()
        self.fill_exterior()

    def find_grid_extents(self):
        h_range = [0, 0]
        v_range = [0, 0]
        h_total = 0
        v_total = 0
        for row in self.file_input:
            dir_str = row[0]
            dist = int(row[1])
            if dir_str == "R":
                h_total += dist
                h_range[1] = max(h_range[1], h_total)
            elif dir_str == "L":
                h_total -= dist
                h_range[0] = min(h_range[0], h_total)
            elif dir_str == "D":
                v_total += dist
                v_range[1] = max(v_range[1], v_total)
            elif dir_str == "U":
                v_total -= dist
                v_range[0] = min(v_range[0], v_total)
        return h_range, v_range

    def tag_nodes(self):
        for row in self.file_input:
            dir_str = row[0]
            dist = int(row[1])
            if dir_str == "R":
                rows = [self.pos[0]]
                cols = range(self.pos[1] + 1, self.pos[1] + 1 + dist)
                self.pos = (self.pos[0], self.pos[1] + dist)
            elif dir_str == "L":
                rows = [self.pos[0]]
                cols = range(self.pos[1] - dist, self.pos[1])
                self.pos = (self.pos[0], self.pos[1] - dist)
            elif dir_str == "D":
                rows = range(self.pos[0] + 1, self.pos[0] + 1 + dist)
                cols = [self.pos[1]]
                self.pos = (self.pos[0] + dist, self.pos[1])
            elif dir_str == "U":
                rows = range(self.pos[0] - dist, self.pos[0])
                cols = [self.pos[1]]
                self.pos = (self.pos[0] - dist, self.pos[1])
            for row, col in list(itertools.product(rows, cols)):
                self.grid[row, col] = 1

    def display_grid(self):
        print(np.where(self.grid, "#", "."))

    def fill_exterior(self):
        nearby_grid = support.find_nearby_coordinates(self.grid)
        nodes = [(0, 0)]
        while nodes:
            next_nodes = []
            for node in nodes:
                nearby_idxs = nearby_grid[node]
                for nearby_idx in nearby_idxs:
                    if self.grid[nearby_idx] == 0:
                        self.grid[nearby_idx] = 2
                        next_nodes.append(nearby_idx)
            nodes = next_nodes
        self.grid = np.where(self.grid == 0, 3, self.grid)
        self.grid = np.where(self.grid == 2, 0, self.grid)

    def count_lava(self):
        return self.grid[self.grid > 0].size


filename = r"year_2023/tests/test_inputs/18_test_input.txt"
# filename = r"year_2023/input/18_inside_fill.txt"
m = ClassName(filename)
m.display_grid()
# m.grid
