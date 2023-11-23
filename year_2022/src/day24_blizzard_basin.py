from AdventOfCode.support import support
import numpy as np


class Blizzard:
    def __init__(self, filename):
        self.file_input = np.array(support.read_input(filename, flavor="str_grid"))
        self.file_input = self.file_input[1:-1, 1:-1]
        self.blizzards = self.create_empty_array()
        for index, item in np.ndenumerate(self.file_input):
            if item == ".":
                self.blizzards[index] = []
            else:
                self.blizzards[index] = [item]
        self.access = np.empty(self.file_input.shape, dtype=bool)
        self.access[:] = False
        self.time = 0
        self.blizzard_def = {
            ">": (0, 1),
            "<": (0, -1),
            "^": (-1, 0),
            "v": (1, 0),
        }

        # This tells where to go.
        # 99 means don't change this index value
        self.blizzard_loop = {
            # Change index[1] to 0. Leave index[0] as is.
            ">": (9999, 0),
            # Change index[1] to end of array. Leave index[0] as is.
            "<": (
                9999,
                self.blizzards.shape[1] - 1,
            ),
            # Change index[0] to end of array. Leave index[1] as is.
            "^": (
                self.blizzards.shape[0] - 1,
                9999,
            ),
            # Change index[0] to 0. Leave index[1] as is.
            "v": (0, 9999),
        }

        while not self.access[-1, -1]:
            self.time += 1
            self.move_blizzard()
            if not self.blizzards[0, 0]:
                self.access[0, 0] = True
            self.find_path()
        self.access = np.empty(self.file_input.shape, dtype=bool)
        self.access[:] = False
        self.time_part1 = self.time
        print(self.time_part1)
        while not self.access[0, 0]:
            self.time += 1
            self.move_blizzard()
            if not self.blizzards[-1, -1]:
                self.access[-1, -1] = True
            self.find_path()
        self.access = np.empty(self.file_input.shape, dtype=bool)
        self.access[:] = False
        b = self.time
        print(b - self.time_part1)
        while not self.access[-1, -1]:
            self.time += 1
            self.move_blizzard()
            if not self.blizzards[0, 0]:
                self.access[0, 0] = True
            self.find_path()
        c = self.time
        print(c - b)

    def move_blizzard(self):
        new_blizzards = self.create_empty_array()
        for index, dirs in np.ndenumerate(self.blizzards):
            if dirs:
                for dir in dirs:
                    new_pos = (
                        index[0] + self.blizzard_def[dir][0],
                        index[1] + self.blizzard_def[dir][1],
                    )
                    if support.point_out_of_bounds(
                        new_pos[0], new_pos[1], self.blizzards
                    ):
                        loop_pos = self.blizzard_loop[dir]
                        if loop_pos[0] < 1000:
                            new_pos = (loop_pos[0], new_pos[1])
                        elif loop_pos[1] < 1000:
                            new_pos = (new_pos[0], loop_pos[1])
                    new_blizzards[new_pos].append(dir)
        self.blizzards = new_blizzards

    def create_empty_array(self):
        empty_grid = np.empty(self.file_input.shape, dtype=list)
        for index, _ in np.ndenumerate(empty_grid):
            empty_grid[index] = []
        return empty_grid

    def find_path(self):
        # Create access array for next time step
        new_access = np.empty(self.file_input.shape, dtype=bool)
        new_access[:] = False

        # Find indices where self.access is true for the previous time step
        current_access_locs = [tuple(x) for x in np.column_stack(np.where(self.access))]

        # For each index where we have access previously
        for index in current_access_locs:
            # Find that index and adjacent indices
            nearby_locs = support.list_ordinal_adjacent(index) + [index]
            nearby_locs = [
                x
                for x in nearby_locs
                if not support.point_out_of_bounds(x[0], x[1], self.access)
            ]
            for nearby in nearby_locs:
                # If a blizzard isn't at that location
                if not self.blizzards[nearby]:
                    new_access[nearby] = True

        self.access = new_access
