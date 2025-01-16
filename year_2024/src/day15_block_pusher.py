from support import support
import numpy as np


class ClassName:
    def __init__(self, filename, part2=False):
        self.part2 = part2
        self.read_input(filename)
        self.direction_dict = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

    def read_input(self, filename):
        self.file_input = support.read_input(filename, flavor="str_grid")
        empty_row = [i for i, lst in enumerate(self.file_input) if not lst][0]
        self.grid = np.array(self.file_input[:empty_row])
        self.directions = self.file_input[empty_row + 1 :]
        self.directions = [item for sublist in self.directions for item in sublist]
        self.direction = self.directions[0]
        if self.part2:
            self.grid = np.array(
                [[item for item in row for _ in range(2)] for row in self.grid]
            )
            at_positions = np.argwhere(self.grid == "@")
            self.grid[tuple(at_positions[1])] = "."
            for row in range(self.grid.shape[0]):
                for col in range(self.grid.shape[1]):
                    if self.grid[row][col] == "O":
                        self.grid[row][col] = "["
                        self.grid[row][col + 1] = "]"

    def update_object_position(self, old_location, new_location):
        obj_type = self.grid[old_location]
        if obj_type[0] in "[]":
            left_pos, right_pos = self.find_other_box_position(old_location)
            left_new_pos = support.sum_tuples(
                left_pos, self.direction_dict[self.direction]
            )
            right_new_pos = support.sum_tuples(
                right_pos, self.direction_dict[self.direction]
            )
            self.grid[left_pos] = "."
            self.grid[right_pos] = "."
            self.grid[left_new_pos] = "["
            self.grid[right_new_pos] = "]"
        else:
            self.grid[old_location] = "."
            self.grid[new_location] = obj_type

    def find_other_box_position(self, object_location):
        # TODO: we want the output to be nice tuples
        object_type = self.grid[object_location][0]
        if object_type == "[":
            left_pos = object_location
            right_pos = (object_location[0], object_location[1] + 1)
        elif object_type == "]":
            left_pos = (object_location[0], object_location[1] - 1)
            right_pos = object_location
        return left_pos, right_pos

    def try_move_object(self, obj_pos):
        new_pos = support.sum_tuples(obj_pos, self.direction_dict[self.direction])
        obj_type = self.grid[obj_pos][0]
        # If trying to move a large box
        if obj_type in "[]":
            left_pos, right_pos = self.find_other_box_position(obj_pos)
            left_new_pos = support.sum_tuples(
                left_pos, self.direction_dict[self.direction]
            )
            right_new_pos = support.sum_tuples(
                right_pos, self.direction_dict[self.direction]
            )

            if self.direction in "^v":
                # if path is blocked
                if self.grid[left_new_pos] == "#" or self.grid[right_new_pos] == "#":
                    pass
                # if path is free
                elif self.grid[left_new_pos] == "." and self.grid[right_new_pos] == ".":
                    self.update_object_position(left_pos, left_new_pos)
                # if path has a large block in it
                else:
                    if self.grid[left_new_pos][0] in "[]":
                        self.try_move_object(left_new_pos)
                    if self.grid[right_new_pos][0] in "[]":
                        self.try_move_object(right_new_pos)
                    if (
                        self.grid[left_new_pos] == "."
                        and self.grid[right_new_pos] == "."
                    ):
                        self.update_object_position(left_pos, left_new_pos)

            else:
                pass
                # TODO: Implement logic for moving large boxes horizontally
                # if moving left then just check left side and then move
                if self.direction == "<":
                    obj_pos = left_pos
                    new_pos = left_new_pos
                elif self.direction == ">":
                    obj_pos = right_pos
                    new_pos = right_new_pos
                
                # if path is blocked
                if self.grid[new_pos] == "#":
                    pass
                # if path is free
                elif self.grid[new_pos] == ".":
                    self.update_object_position(obj_pos, new_pos)
                # if path has a block
                elif self.grid[new_pos][0] in "O[]":
                    self.try_move_object(new_pos)
                    if self.grid[new_pos] == ".":
                        self.update_object_position(obj_pos, new_pos)
                # if moving right then just check right side and then move
        # If trying to move a small box/robot
        else:
            # if path is blocked
            if self.grid[new_pos] == "#":
                pass
            # if path is free
            elif self.grid[new_pos] == ".":
                self.update_object_position(obj_pos, new_pos)
            # if path has a block
            elif self.grid[new_pos][0] in "O[]":
                self.try_move_object(new_pos)
                if self.grid[new_pos] == ".":
                    self.update_object_position(obj_pos, new_pos)

    def sum_box_gps(self):
        gps_sum = 0
        box_positions = np.argwhere(np.isin(self.grid, ["O", "["]))
        for box_position in box_positions:
            gps_sum += box_position[0] * 100 + box_position[1]
        return gps_sum

    def move_robot_all_instructions(self):
        for direction in self.directions:
            self.direction = direction
            self.print_grid()
            print(direction)
            robot_pos = np.where(self.grid == "@")
            self.try_move_object(robot_pos)

    def print_grid(self):
        for row in self.grid:
            print("".join(row))


filename = r"year_2024/tests/test_inputs/15_test_input.txt"
# filename = r"year_2024/input/15_block_pusher.txt"
m = ClassName(filename, part2=True)
m.move_robot_all_instructions()
m.sum_box_gps()
