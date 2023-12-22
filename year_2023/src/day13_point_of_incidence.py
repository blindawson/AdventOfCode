from AdventOfCode.support import support
import numpy as np


class ClassName:
    def __init__(self, filename, part2=False):
        self.file_input = support.read_input(filename, flavor=None, split_char=None)
        self.part2 = part2
        self.grids = self.split_input()

    def sum_grids(self):
        s = 0
        for g in self.grids:
            dstr, didx = self.find_crease(g)
            if dstr == "row":
                s += didx * 100
            else:
                s += didx
        return s

    def split_input(self):
        grids = []
        while "" in self.file_input:
            blank_index = self.file_input.index("")
            grid = [[i for i in x] for x in self.file_input[:blank_index]]
            grids.append(np.array(grid))
            self.file_input = self.file_input[blank_index + 1 :]
        return grids

    def reverse_array(self, a):
        return a[::-1]

    def find_crease(self, grid: np.array):
        rowcol_dict = {"row": grid, "col": grid.T}
        # Direction strings and grids
        for dstr, dgrid in rowcol_dict.items():
            for y in range(len(dgrid) - 1):
                if not self.part2:
                    if np.array_equal(dgrid[y], dgrid[y + 1]):
                        top_half = dgrid[: y + 1]
                        bottom_half = self.reverse_array(dgrid[y + 1 :])
                        min_len = min(len(top_half), len(bottom_half))
                        top_half = top_half[-min_len:]
                        bottom_half = bottom_half[-min_len:]
                        if np.array_equal(top_half, bottom_half):
                            return dstr, y + 1
                else:
                    if np.count_nonzero(dgrid[y] != dgrid[y + 1]) <= 1:
                        top_half = dgrid[: y + 1]
                        bottom_half = self.reverse_array(dgrid[y + 1 :])
                        min_len = min(len(top_half), len(bottom_half))
                        top_half = top_half[-min_len:]
                        bottom_half = bottom_half[-min_len:]
                        if np.count_nonzero(top_half != bottom_half) == 1:
                            print(dstr, y + 1)
                            return dstr, y + 1
        raise ValueError("Crease not found")
