from AdventOfCode.support import support
import numpy as np


class Lava:
    def __init__(self, filename):
        self.file_input = support.read_input(
            filename, flavor="split_int", split_char=","
        )
        self.read_input()
        self.count_adjacent()

    def read_input(self) -> None:
        max_x = max([i[0] for i in self.file_input])
        max_y = max([i[1] for i in self.file_input])
        max_z = max([i[2] for i in self.file_input])
        self.grid = np.zeros([max_x + 1, max_y + 1, max_z + 1], dtype=int)

        for i in self.file_input:
            self.grid[i] = 16

    def count_adjacent(self) -> None:
        for x in range(self.grid.shape[0]):
            for y in range(self.grid.shape[1]):
                for z in range(self.grid.shape[2]):
                    cube_loc = (x, y, z)
                    if self.grid[cube_loc] > 0:
                        nearby_locs = [
                            (x - 1, y, z),
                            (x + 1, y, z),
                            (x, y - 1, z),
                            (x, y + 1, z),
                            (x, y, z - 1),
                            (x, y, z + 1),
                        ]

                        for nearby_loc in nearby_locs:
                            out_of_bounds = support.point_out_of_bounds_3D(
                                x=nearby_loc[0],
                                y=nearby_loc[1],
                                z=nearby_loc[2],
                                grid=self.grid,
                            )
                            if not out_of_bounds:
                                if self.grid[nearby_loc] > 0:
                                    self.grid[cube_loc] -= 1

    def sum_cube_faces(self) -> int:
        grid_sum = self.grid.sum()
        grid_count = np.count_nonzero(self.grid)
        grid_sum -= grid_count * 10
        return grid_sum


filename = r"year_2022/tests/test_inputs/18_test_input.txt"
r = Lava(filename)
r.grid
