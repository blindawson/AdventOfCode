from AdventOfCode.support import support
import itertools
import numpy as np


class ClassName:
    def __init__(self, filename, part2=False):
        self.file_input = np.array(
            support.read_input(filename, flavor="split", split_char=" ")
        )

        dir_dict = {0: "R", 1: "D", 2: "L", 3: "U"}
        if part2:
            self.file_input[:, 1] = [int(x[2:-2], 16) for x in self.file_input[:, 2]]
            self.file_input[:, 0] = [
                dir_dict[int(x[-2])] for x in self.file_input[:, 2]
            ]

        self.pos = (0, 0)
        self.boundary_points = sum([int(x) for x in self.file_input[:, 1]])
        self.area = self.shoelace()
        self.interior_points = self.area + 1 - self.boundary_points / 2

        # Pick's Theorem
        self.total_points = int(self.interior_points + self.boundary_points)

    # Area of shape
    def shoelace(self):
        sum_area = 0
        for row in self.file_input:
            dir_str = row[0]
            dist = int(row[1])
            if dir_str == "R":
                new_pos = (self.pos[0], self.pos[1] + dist)
            elif dir_str == "L":
                new_pos = (self.pos[0], self.pos[1] - dist)
            elif dir_str == "D":
                new_pos = (self.pos[0] + dist, self.pos[1])
            elif dir_str == "U":
                new_pos = (self.pos[0] - dist, self.pos[1])
            height = (self.pos[0] + new_pos[0]) / 2
            width = new_pos[1] - self.pos[1]
            area = height * width
            sum_area += area
            print(new_pos, area)

            self.pos = new_pos
        return sum_area * -1
