from support import support
import numpy as np


class ClassName:
    def __init__(self, filename):
        self.file_input = np.array(support.read_input(filename, flavor="str_grid"))
        self.reset_guard()

    def reset_guard(self):
        self.guard_loc = np.where(self.file_input == "^")
        self.guard_loc = (self.guard_loc[0][0], self.guard_loc[1][0])
        self.guard_dir = "N"
        self.walked_grid = np.zeros(self.file_input.shape)
        self.walked_grid[self.guard_loc] = 1

    def move_guard_once(self, grid):
        next_position = support.sum_tuples(
            self.guard_loc, support.direction_dict[self.guard_dir]
        )
        if support.point_out_of_bounds(next_position[0], next_position[1], grid):
            self.next_position_in_bounds = False
        elif grid[next_position] == "#":
            self.guard_dir = support.turn_right_dict[self.guard_dir]
        else:
            self.guard_loc = next_position
            self.walked_grid[next_position] = 1

    def part1(self):
        self.next_position_in_bounds = True
        while self.next_position_in_bounds:
            self.move_guard_once(self.file_input)

        return int(self.walked_grid.sum())

    def part2(self):
        loop_inserts = 0

        self.part1()
        walked_grid_copy = self.walked_grid.copy()
        it = np.nditer(self.file_input, flags=["multi_index"])
        for x in it:
            if x.item() in "#^":
                continue
            if walked_grid_copy[it.multi_index] == 0:
                continue

            self.reset_guard()
            print(it.multi_index)

            new_grid = self.file_input.copy()
            new_grid[it.multi_index] = "#"

            self.guard_dir_grid = np.full(new_grid.shape, "", dtype=str)

            self.next_position_in_bounds = True
            distance = 0
            while self.next_position_in_bounds:
                if self.guard_dir not in self.guard_dir_grid[self.guard_loc]:
                    self.guard_dir_grid[self.guard_loc] += self.guard_dir
                else:
                    loop_inserts += 1
                    break
                self.move_guard_once(new_grid)

                distance += 1
                if distance > self.file_input.size:
                    raise AttributeError("Loop Encountered.")

        return loop_inserts
