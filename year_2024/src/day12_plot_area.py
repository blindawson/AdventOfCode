from support import support
import numpy as np


class ClassName:
    def __init__(self, filename):
        self.file_input = np.array(support.read_input(filename, flavor="str_grid"))
        self.checked = self.create_zeros_grid()

    def create_zeros_grid(self):
        return np.zeros(self.file_input.shape)

    def find_plot_indices(self, idx, plant_type):
        plot_grid = self.create_zeros_grid()
        plot_grid[idx] = 1
        # 0 means we haven't checked it yet
        # 1 means it's part of the plot
        # 2 means it's not part of the plot

        neighbors = support.list_neighbors(idx, self.file_input)
        while neighbors:
            neighbor = neighbors.pop()
            if self.file_input[neighbor] == plant_type:
                plot_grid[neighbor] = 1
                self.checked[neighbor] = 1
                # then pull all those neighbors
                new_neighbors = support.list_neighbors(neighbor, self.file_input)
                # remove any that are already in the plot (1) or checked (2)
                new_neighbors = [n for n in new_neighbors if plot_grid[n] == 0]
                # remove duplicates
                neighbors = list(set(neighbors + new_neighbors))
            else:
                plot_grid[neighbor] = 2
        # reset all 2's to 0's
        plot_grid[plot_grid == 2] = 0
        return plot_grid

    def plot_area(self, plot_grid):
        return int(np.sum(plot_grid))

    def plot_perimeter(self, plot_grid):
        perimeter = 0
        indices = np.argwhere(plot_grid == 1)
        for idx in indices:
            perimeter += 4
            perimeter -= len(
                [n for n in support.list_neighbors(idx, plot_grid) if plot_grid[n] == 1]
            )
        return perimeter

    def plot_sides(self, plot_grid):
        sides = self.plot_perimeter(plot_grid)
        indices = np.argwhere(plot_grid == 1)
        sides_grid = np.full(plot_grid.shape, "", dtype=object)
        # for each index in the plot grid
        for idx in indices:
            # for each direction
            for key, value in support.direction_dict.items():
                row = idx[0] + value[0]
                col = idx[1] + value[1]
                # if there is a fence in that direction
                if (
                    support.point_out_of_bounds(row, col, plot_grid)
                    or plot_grid[row, col] == 0
                ):
                    # add that direction to sides_grid
                    sides_grid[tuple(idx)] += key
        for idx in indices:
            west_idx = (idx[0], idx[1] - 1)
            north_idx = (idx[0] - 1, idx[1])
            dir_list = [
                ("N", west_idx),
                ("S", west_idx),
                ("E", north_idx),
                ("W", north_idx),
            ]
            for direction, neighbor in dir_list:
                if (
                    direction in sides_grid[tuple(idx)]
                    and not support.point_out_of_bounds(None, None, plot_grid, neighbor)
                    and direction in sides_grid[neighbor]
                ):
                    sides -= 1

        return sides

    def fence_price(self, part2=False):
        total_fence_price = 0
        for i, row in enumerate(self.file_input):
            for j, plant_type in enumerate(row):
                idx = (i, j)
                if self.checked[idx] == 0:
                    plot_grid = self.find_plot_indices(idx, plant_type)
                    plot_area = self.plot_area(plot_grid)
                    plot_perimeter = self.plot_perimeter(plot_grid)
                    plot_sides = self.plot_sides(plot_grid)
                    if part2:
                        plot_perimeter = plot_sides
                    total_fence_price += plot_perimeter * plot_area
        return int(total_fence_price)
