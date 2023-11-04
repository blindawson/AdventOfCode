from AdventOfCode.support import support
import numpy as np


class Lava:
    def __init__(self, filename, part2: bool = False):
        self.file_input = support.read_input(
            filename, flavor="split_int", split_char=","
        )
        self.part2 = part2
        self.read_input()
        if self.part2:
            self.group_air_cubes()
        self.scan_grid()

    def read_input(self) -> None:
        max_x = max([i[0] for i in self.file_input])
        max_y = max([i[1] for i in self.file_input])
        max_z = max([i[2] for i in self.file_input])
        self.grid = np.zeros([max_x + 1, max_y + 1, max_z + 1], dtype=int)

        for i in self.file_input:
            self.grid[i] = 16

    def nearby_locs(self, x: int, y: int, z: int) -> list[tuple[int, int, int]]:
        return [
            (x - 1, y, z),
            (x + 1, y, z),
            (x, y - 1, z),
            (x, y + 1, z),
            (x, y, z - 1),
            (x, y, z + 1),
        ]

    def scan_grid(self) -> None:
        for x in range(self.grid.shape[0]):
            for y in range(self.grid.shape[1]):
                for z in range(self.grid.shape[2]):
                    cube_loc = (x, y, z)
                    if self.grid[cube_loc] > 5:
                        for nearby_loc in self.nearby_locs(x, y, z):
                            out_of_bounds = support.point_out_of_bounds_3D(
                                x=nearby_loc[0],
                                y=nearby_loc[1],
                                z=nearby_loc[2],
                                grid=self.grid,
                            )
                            if not out_of_bounds:
                                if self.grid[nearby_loc] > 1:
                                    self.grid[cube_loc] -= 1

    def group_air_cubes(self) -> None:
        air_locs = np.where(self.grid == 0)
        for a in range(len(air_locs[0])):
            air_loc = air_locs[0][a], air_locs[1][a], air_locs[2][a]
            _ = self.review_air_locs(air_loc)

    def review_air_locs(
        self, cube_loc: tuple[int, int, int], exterior_air: bool = False
    ) -> bool:
        if self.grid[cube_loc] == 0:
            self.grid[cube_loc] = self.air_code
            x, y, z = cube_loc
            for nearby_loc in self.nearby_locs(x, y, z):
                out_of_bounds = support.point_out_of_bounds_3D(
                    x=nearby_loc[0],
                    y=nearby_loc[1],
                    z=nearby_loc[2],
                    grid=self.grid,
                )
                if not out_of_bounds:
                    if self.grid[nearby_loc] == 0:
                        self.grid[cube_loc] = 3
                else:
                    self.air_code_reading[self.air_code] = "Exterior"
            if exterior_air:
                self.grid[cube_loc] = 1
            else:
                self.grid[cube_loc] = 2
        return exterior_air

    def fill_exterior(self) -> None:
        # Turn the edges of the grid from 0 to 1
        grid_edges = [
            self.grid[0, :, :],
            self.grid[:, 0, :],
            self.grid[:, :, 0],
            self.grid[-1, :, :],
            self.grid[:, -1, :],
            self.grid[:, :, -1],
        ]
        exterior_air = []
        for grid_edge in grid_edges:
            grid_edge[grid_edge == 0] = 1
            coordinates = np.argwhere(grid_edge == 1)
            exterior_air += [tuple(coord) for coord in coordinates]

        while self.exterior_air:
            adjacent_air = []
            for e in exterior_air:
                x, y, z = e
                for nearby_loc in self.nearby_locs(x, y, z):
                    out_of_bounds = support.point_out_of_bounds_3D(
                        x=nearby_loc[0],
                        y=nearby_loc[1],
                        z=nearby_loc[2],
                        grid=self.grid,
                    )
                    if not out_of_bounds:
                        if self.grid[nearby_loc] == 0:
                            adjacent_air.append(nearby_loc)
                            nearby_loc = 1

    def sum_cube_faces(self) -> int:
        if self.part2:
            grid_sum = np.sum(self.grid[self.grid > 5])
        else:
            grid_sum = self.grid.sum()
        grid_count = np.sum(self.grid > 5)
        grid_sum -= grid_count * 10
        return grid_sum


# filename = r"year_2022/tests/test_inputs/18_test_input.txt"
# filename = r"year_2022/input/18_boiling_boulders.txt"
# r = Lava(filename, part2=False)
# print(r.sum_cube_faces())
# r.fill_exterior()
