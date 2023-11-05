from AdventOfCode.support import support
import numpy as np


class Lava:
    """
    Grid of locations.
    Air is initialized to 0.
        Exterior air is changed to 1.
        Interior air is changed to 2.
    Lava is initialized to 16 (10 + 6 faces)
        Part 1: Lava is reduced by 1 for each face touching other lava.
        Part 2: Lava is reduced by 1 for each face touching other lava or interior air.
    """

    def __init__(self, filename, part2: bool = False):
        self.file_input = support.read_input(
            filename, flavor="split_int", split_char=","
        )
        self.read_input()
        if part2:
            self.fill_exterior()
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

    # Adjust lava values down for each nearby lava
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

    # Turn the edges of the grid from 0 to 1
    # Then turn adjacent 0s to 1s and so on
    def fill_exterior(self) -> None:
        grid_edges = [
            self.grid[0, :, :],
            self.grid[-1, :, :],
            self.grid[:, 0, :],
            self.grid[:, -1, :],
            self.grid[:, :, 0],
            self.grid[:, :, -1],
        ]
        exterior_air = []
        for i, grid_edge in enumerate(grid_edges):
            grid_edge[grid_edge == 0] = 1
            coordinates = np.argwhere(grid_edge == 1)
            if i == 0:
                coordinates = [[0] + list(coordinate) for coordinate in coordinates]
            elif i == 1:
                coordinates = [
                    [self.grid.shape[0] - 1] + list(coordinate)
                    for coordinate in coordinates
                ]
            elif i == 2:
                coordinates = [
                    [coordinate[0]] + [0] + [coordinate[1]]
                    for coordinate in coordinates
                ]
            elif i == 3:
                coordinates = [
                    [coordinate[0]] + [self.grid.shape[0] - 1] + [coordinate[1]]
                    for coordinate in coordinates
                ]
            elif i == 4:
                coordinates = [list(coordinate) + [0] for coordinate in coordinates]
            elif i == 5:
                coordinates = [
                    list(coordinate) + [self.grid.shape[0] - 1]
                    for coordinate in coordinates
                ]
            exterior_air += [tuple(coord) for coord in coordinates]

        while exterior_air:
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
                            self.grid[nearby_loc] = 1
            exterior_air = list(set(adjacent_air))
        self.grid[self.grid == 0] = 2

    def sum_cube_faces(self) -> int:
        grid_sum = np.sum(self.grid[self.grid > 5])
        grid_count = np.sum(self.grid > 5)
        grid_sum -= grid_count * 10
        return grid_sum
