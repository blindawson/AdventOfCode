from AdventOfCode.support import support
import numpy as np


class ClassName:
    def __init__(self, filename, loop_length=0):
        self.grid = np.array(support.read_input(filename, flavor="str_grid"))
        self.loads = []
        self.loop_length = loop_length
        self.jumped_forward = False
        if not loop_length:
            for idx in np.ndindex(self.grid.shape):
                self.move_rock(idx)
        else:
            i = 1
            while i < loop_length:
                for tilt_dir in ["N", "W", "S", "E"]:
                    if tilt_dir in ["N", "W"]:
                        for idx in np.ndindex(self.grid.shape):
                            self.move_rock(idx, tilt_dir)
                    else:
                        rows, cols = self.grid.shape
                        for y in range(rows - 1, -1, -1):
                            for x in range(cols - 1, -1, -1):
                                idx = (y, x)
                                self.move_rock(idx, tilt_dir)
                # print(self.grid)
                self.loads.append(self.calc_load())
                print(self.calc_load())
                # print(np.count_nonzero(self.grid == "O"))
                found_loop = self.find_output_loop(self.loads)
                if found_loop and not self.jumped_forward:
                    i += found_loop
                    self.jumped_forward = True
                else:
                    i += 1

    def calc_load(self):
        s = 0
        for idx, item in enumerate(support.reverse_array(self.grid)):
            multiplier = idx + 1
            rock_count = np.count_nonzero(item == "O")
            s += multiplier * rock_count
        return s

    def move_rock(self, idx: tuple, dir: str = "N"):
        if not self.on_edge(dir, idx, self.grid):
            move_idx = support.sum_tuples(idx, support.direction_dict[dir])
            if (self.grid[idx] == "O") and (self.grid[move_idx] == "."):
                self.grid[move_idx] = "O"
                self.grid[idx] = "."
                self.move_rock(move_idx, dir)

    def on_edge(self, dir: str, idx: tuple, grid: list):
        if (dir == "N") and (idx[0] == 0):
            return True
        elif (dir == "S") and (idx[0] == len(grid) - 1):
            return True
        elif (dir == "W") and (idx[1] == 0):
            return True
        elif (dir == "E") and (idx[1] == len(grid[0]) - 1):
            return True
        else:
            return False

    def find_output_loop(self, load_list):
        new_load = load_list[-1]
        # print(load_list.count(new_load))
        if load_list.count(new_load) >= 4:
            idx1 = len(load_list) - 1
            idx2 = idx1 - load_list[:-1][::-1].index(new_load) - 1
            idx3 = idx2 - load_list[:idx2][::-1].index(new_load) - 1
            idx4 = idx3 - load_list[:idx3][::-1].index(new_load) - 1
            if (idx1 - idx2 == idx2 - idx3) and (idx1 - idx2 == idx3 - idx4):
                repeat_length = idx1 - idx2
                remaining_loops = self.loop_length - idx1
                added_loops = int(remaining_loops / repeat_length)
                return added_loops * repeat_length
        return 0
