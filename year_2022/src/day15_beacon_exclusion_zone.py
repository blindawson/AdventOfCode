import re
import numpy as np
import matplotlib.pyplot as plt


class BeaconZone:
    def __init__(self, filename):
        self.file_input = open(filename).read().splitlines()
        self.read_input()
        self.sensors = list(self.input.keys())
        self.beacons = list(set(self.input.values()))
        self.find_grid_edges()
        grid_shape = (
            self.yrange[1] - self.yrange[0] + 1,
            self.xrange[1] - self.xrange[0] + 1,
        )
        self.grid = np.empty(grid_shape, dtype=str)
        self.assign_positions()
        self.mark_searched()

    def read_input(self):
        self.input = {}
        pattern = r"x=(-?\d+), y=(-?\d+)"
        for row in self.file_input:
            matches = re.findall(pattern, row)
            match1 = (int(matches[0][1]), int(matches[0][0]))
            match2 = (int(matches[1][1]), int(matches[1][0]))
            self.input[match1] = match2

    def manhattan_distance(self, coordinate1, coordinate2):
        y1, x1 = coordinate1
        y2, x2 = coordinate2
        return abs(x1 - x2) + abs(y1 - y2)

    def find_grid_edges(self):
        xs = [x[1] for x in self.input.keys()] + [x[1] for x in self.input.values()]
        ys = [x[0] for x in self.input.keys()] + [x[0] for x in self.input.values()]
        self.xrange = (min(xs), max(xs))
        self.yrange = (min(ys), max(ys))

    def assign_positions(self):
        for s in self.sensors:
            self.grid[s] = "S"
        for b in self.beacons:
            self.grid[b] = "B"

    def mark_searched(self):
        for sensor in self.sensors:
            dist = self.manhattan_distance(sensor, self.input[sensor])
            for y in range(sensor[0] - dist, sensor[0] + dist + 1):
                for x in range(sensor[1] - dist, sensor[1] + dist + 1):
                    print(y, x)
                    if x >= self.xrange[0] and x <= self.xrange[1]:
                        if y >= self.yrange[0] and y <= self.yrange[1]:
                            if self.manhattan_distance(sensor, (y, x)) <= dist:
                                if not self.grid[(y, x)]:
                                    self.grid[(y, x)] = "#"

    def plot(self):
        # Create a mapping of unique strings to numerical values
        value_map = {"S": 1, "B": 2, "#": 3, "": 0}

        # Convert the grid to numerical values using the mapping
        numerical_grid = np.vectorize(value_map.get)(self.grid)

        # Plot the grid
        plt.imshow(numerical_grid, cmap="viridis")
        plt.colorbar(ticks=sorted(value_map.values()))
        plt.show()
        
    def count_positions(self, row):
        return list(self.grid[row, :]).count("#")


# filename = r"year_2022/tests/test_inputs/15_test_input.txt"
# filename = r'year_2022/input/15_beacon_exclusion_zone.txt'
# b = BeaconZone(filename)
# b.plot()
