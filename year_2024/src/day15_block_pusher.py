from support import support
import numpy as np


class ClassName:
    def __init__(self, filename):
        self.read_input(filename)
        self.direction_dict = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

    def read_input(self, filename):
        self.file_input = support.read_input(filename, flavor="str_grid")
        empty_row = [i for i, lst in enumerate(self.file_input) if not lst][0]
        self.grid = np.array(self.file_input[:empty_row])
        self.directions = self.file_input[empty_row + 1 :]
        self.directions = [item for sublist in self.directions for item in sublist]

    def move_robot(self, direction):
        robot_pos = np.where(self.grid == "@")
        new_pos = support.sum_tuples(robot_pos, self.direction_dict[direction])
        if self.grid[new_pos] == "#":
            # don't move
            pass
        elif self.grid[new_pos] == ".":
            self.grid[robot_pos] = "."
            self.grid[new_pos] = "@"
        elif self.grid[new_pos] == "O":
            moving_space, new_values = self.moving_space_coordinates(direction)
            # if space, move boxes and robot
            if moving_space:
                for space, value in zip(moving_space, new_values[0]):
                    self.grid[space] = value
            # if no space, don't move

    def box_gps(self, coord):
        return coord[0] * 100 + coord[1]

    def moving_space_coordinates(self, direction):
        robot_pos = np.where(self.grid == "@")
        robot_pos = (robot_pos[0][0], robot_pos[1][0]) 
        new_pos = support.sum_tuples(robot_pos, self.direction_dict[direction])
        moving_coordinates = []
        new_values = []
        if direction == "<":
            row = robot_pos[0]
            for col in range(new_pos[1], 0, -1):
                if self.grid[row, col] == ".":
                    # change [.OO@] to [OO@.]
                    # moving_coordinates are indices from . to @
                    moving_coordinates = [(row, c) for c in range(col, robot_pos[1] + 1)]
                    new_values = [["O"]*(len(moving_coordinates)-2) + ["@","."]]
                    break
                elif self.grid[row, col] == "#":
                    break
                elif self.grid[row, col] == "O":
                    continue
        elif direction == ">":
            row = robot_pos[0]
            for col in range(new_pos[1], self.grid.shape[1]):
                if self.grid[row, col] == ".":
                    # change [@OO.] to [.@OO]
                    # moving_coordinates are indices from . to @
                    moving_coordinates = [(row, c) for c in range(robot_pos[1], col + 1)]
                    new_values = [[".","@"] + ["O"]*(len(moving_coordinates)-2)]
                    break
                elif self.grid[row, col] == "#":
                    break
                elif self.grid[row, col] == "O":
                    continue
        elif direction == "^":
            col = robot_pos[1]
            for row in range(new_pos[0], 0, -1):
                if self.grid[row, col] == ".":
                    # change [.      [O
                    #         O   to  O
                    #         O       @
                    #         @]      .]
                    # moving_coordinates are indices from . to @
                    moving_coordinates = [(r, col) for r in range(row, robot_pos[0] + 1)]
                    new_values = [["O"]*(len(moving_coordinates)-2) + ["@","."]]
                    break
                elif self.grid[row, col] == "#":
                    break
                elif self.grid[row, col] == "O":
                    continue
        elif direction == "v":
            col = robot_pos[1]
            for row in range(new_pos[0], self.grid.shape[0]):
                if self.grid[row, col] == ".":
                    # change [@      [.
                    #         O   to  @
                    #         O       O
                    #         .]      O]
                    # moving_coordinates are indices from . to @
                    moving_coordinates = [(r, col) for r in range(robot_pos[0], row + 1)]
                    new_values = [[".","@"] + ["O"]*(len(moving_coordinates)-2)]
                    break
                elif self.grid[row, col] == "#":
                    break
                elif self.grid[row, col] == "O":
                    continue
        return moving_coordinates, new_values

    def part1(self):
        for direction in self.directions:
            self.move_robot(direction)
            print(direction)
            print(self.grid)
        box_positions = np.argwhere(self.grid == "O")
        gps_sum = 0
        for box_position in box_positions:
            gps_sum += self.box_gps(box_position)
        return gps_sum

    def part2(self):
        pass


filename = r"year_2024/tests/test_inputs/15_test_input.txt"
# filename = r"year_2024/input/15_block_pusher.txt"
m = ClassName(filename)
m.part1()
