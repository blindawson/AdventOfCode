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
        self.access_times = self.create_empty_array()
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
        
        self.move_blizzards()

    def move_blizzards(self):
        self.time += 1
        new_blizzards = self.create_empty_array()
        for index, dirs in np.ndenumerate(self.blizzards):
            if dirs:
                for dir in dirs:
                    new_pos = (
                        index[0] + self.blizzard_def[dir][0],
                        index[1] + self.blizzard_def[dir][1],
                    )
                    if support.point_out_of_bounds(new_pos[0], new_pos[1], self.blizzards):
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


# I'm imagining an array of dict
# blizzards shows blizzards currently present
# blizzards [">", "<"]
# access_times show the rounds when that space is
# free of blizzards and it's possible to have moved there
# from the start position by that time.
# access_times [1, 4]
# So each round we check where blizzards are not present
# For those locations we see if that location or any adjacent
# location were accessible the previous round. If so it's accessible this round
# Keep adding rounds until the exit is accessible.


filename = r"year_2022/tests/test_inputs/24_test_input.txt"
m = Blizzard(filename)
m.blizzards
