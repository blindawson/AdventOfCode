from AdventOfCode.support import support
import numpy as np


class PipeMaze:
    def __init__(self, filename):
        self.file_input = np.array(support.read_input(filename, flavor="str_grid"))
        self.grid = np.zeros(
            (self.file_input.shape[0] * 2, self.file_input.shape[1] * 2), dtype=str
        )
        for idx, item in np.ndenumerate(self.file_input):
            self.grid[idx[0] * 2, idx[1] * 2] = item
        self.start_loc = tuple([x[0] for x in np.where(self.grid == "S")])
        self.found_loop = False

        previous_loc = self.start_loc
        # for all locations adjacent to starting position
        for loc in self.list_neighbors_double_space(previous_loc, self.grid):
            # Create a loop map starting with the start loc
            self.loop_map = np.zeros(self.grid.shape, dtype=bool)
            self.loop_map[self.start_loc] = True
            while not self.found_loop:
                # Grab the pipe shape at location
                pipe_shape = self.grid[loc]
                # If location has a real pipe
                if pipe_shape in self.pipe_dict.keys():
                    connections = self.find_connections(loc)
                    # If connections include previous location
                    if previous_loc in connections:
                        new_loc = [x for x in connections if not x == previous_loc]
                        # If connections has a new location
                        if new_loc:
                            self.loop_map[loc] = True
                            middle_loc = (
                                int((loc[0] + previous_loc[0]) / 2),
                                int((loc[1] + previous_loc[1]) / 2),
                            )
                            self.loop_map[middle_loc] = True

                            previous_loc = loc
                            loc = new_loc[0]
                            self.found_loop = "S" == self.grid[loc]
                        else:
                            break
                    else:
                        break
                else:
                    break
            if self.found_loop:
                middle_loc = (
                    int((loc[0] + previous_loc[0]) / 2),
                    int((loc[1] + previous_loc[1]) / 2),
                )
                self.loop_map[middle_loc] = True
                break
        self.loop_len = int((self.loop_map.sum()) / 4)

        # Part 2
        # Not Checked: 0
        # Pipe: 1
        # Edge: 2
        self.grid2 = np.zeros(self.grid.shape, dtype=int)
        self.grid2[0, :] = 2
        self.grid2[-1, :] = 2
        self.grid2[:, -1] = 2
        self.grid2[:, 0] = 2
        for idx, item in np.ndenumerate(self.grid2):
            if self.loop_map[idx]:
                self.grid2[idx] = 1
        for idx, item in np.ndenumerate(self.grid2):
            # If location isn't checked
            if item == 2:
                self.find_adjacent(idx)

    pipe_dict = {
        "|": ["N", "S"],
        "-": ["W", "E"],
        "L": ["N", "E"],
        "J": ["N", "W"],
        "7": ["S", "W"],
        "F": ["S", "E"],
    }

    def find_connections(self, loc: tuple):
        pipe = self.grid[loc]
        adjacent_str = self.pipe_dict[pipe]
        adjacent_tuples = [
            support.sum_tuples(
                support.direction_dict[x],
                support.sum_tuples(support.direction_dict[x], loc),
            )
            for x in adjacent_str
        ]
        adjacent_tuples = support.remove_out_of_bounds_coordinates(
            adjacent_tuples, self.grid
        )
        return adjacent_tuples

    def follow_loop(self, loc: tuple):
        if self.grid[loc] == "S":
            self.found_loop = True
        else:
            connections = self.find_connections(loc)
            [self.loop.append(x) for x in connections if x not in self.loop]
            self.follow_loop(self.loop[-1])

    def find_adjacent(self, loc: tuple):
        adjacent_map = np.zeros(self.grid2.shape, dtype=bool)
        adjacent_locs = support.remove_out_of_bounds_coordinates(
            support.list_ordinal_adjacent(loc), self.grid2
        )
        for loc in adjacent_locs:
            adjacent_map[loc] = True
        for idx in adjacent_locs:
            if self.grid2[idx] == 0:
                self.grid2[idx] = 3
                [
                    adjacent_locs.append(x)
                    for x in support.remove_out_of_bounds_coordinates(
                        support.list_ordinal_adjacent(idx), self.grid2
                    )
                    if not adjacent_map[x]
                ]

    def list_neighbors_double_space(self, loc: tuple, grid):
        y, x = loc
        nearby_initial = [(y - 2, x), (y, x - 2), (y + 2, x), (y, x + 2)]
        nearby_initial = support.remove_out_of_bounds_coordinates(nearby_initial, grid)
        return nearby_initial

    def count_spaces(self):
        spaces = 0
        y, x = np.where(self.grid2 == 0)
        for i, j in zip(y, x):
            if (i % 2 == 0) and (j % 2 == 0):
                spaces += 1
        return spaces
