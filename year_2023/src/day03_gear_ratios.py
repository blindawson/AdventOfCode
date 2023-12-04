from AdventOfCode.support import support
import numpy as np


class Gear:
    def __init__(self, filename):
        self.grid = np.array(support.read_input(filename, flavor="str_grid"))
        self.skip_indices = []
        self.sum = 0
        self.gear_dict = {}
        self.double_gear = []
        for index, item in np.ndenumerate(self.grid):
            if item.isnumeric() and index not in self.skip_indices:
                str_num, adjacent_symbol = self.find_number(index, item)
                # print(str_num)
                if adjacent_symbol:
                    self.sum += int(str_num)
                    for i in range(len(str_num)):
                        self.skip_indices.append((index[0], index[1] + i))
        self.skip_indices = []
        for index, item in np.ndenumerate(self.grid):
            if item.isnumeric() and index not in self.skip_indices:
                str_num, adjacent_index = self.find_gear_ratio(index, item)
                # print(str_num)
                if adjacent_index:
                    if adjacent_index not in self.gear_dict.keys():
                        self.gear_dict[adjacent_index] = int(str_num)
                    else:
                        self.gear_dict[adjacent_index] = self.gear_dict[
                            adjacent_index
                        ] * int(str_num)
                        self.double_gear.append(adjacent_index)
                    for i in range(len(str_num)):
                        self.skip_indices.append((index[0], index[1] + i))
        self.gear_dict_sum = sum([self.gear_dict[x] for x in self.double_gear])

    def find_number(self, index, str_num, adjacent_symbol=False):
        nearby_locs = support.list_all_adjacent(index)
        nearby_locs = [
            x
            for x in nearby_locs
            if not support.point_out_of_bounds(x[0], x[1], self.grid)
        ]
        for nearby in nearby_locs:
            if not self.grid[nearby] == "." and not self.grid[nearby].isnumeric():
                adjacent_symbol = True

        next_index = (index[0], index[1] + 1)
        if not support.point_out_of_bounds(next_index[0], next_index[1], self.grid):
            if self.grid[next_index].isnumeric():
                str_num += self.grid[next_index]
                str_num, adjacent_symbol = self.find_number(
                    next_index, str_num, adjacent_symbol
                )
        return str_num, adjacent_symbol

    def find_gear_ratio(self, index, str_num, adjacent_index=False):
        nearby_locs = support.list_all_adjacent(index)
        nearby_locs = [
            x
            for x in nearby_locs
            if not support.point_out_of_bounds(x[0], x[1], self.grid)
        ]
        for nearby in nearby_locs:
            if self.grid[nearby] == "*":
                adjacent_index = nearby

        next_index = (index[0], index[1] + 1)
        if not support.point_out_of_bounds(next_index[0], next_index[1], self.grid):
            if self.grid[next_index].isnumeric():
                str_num += self.grid[next_index]
                str_num, adjacent_index = self.find_gear_ratio(
                    next_index, str_num, adjacent_index
                )
        return str_num, adjacent_index
