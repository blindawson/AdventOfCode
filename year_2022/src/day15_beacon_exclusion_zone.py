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

    def read_input(self):
        self.input = {}
        self.sensor_ranges = {}
        pattern = r"x=(-?\d+), y=(-?\d+)"
        for row in self.file_input:
            matches = re.findall(pattern, row)
            sensor = (int(matches[0][1]), int(matches[0][0]))
            beacon = (int(matches[1][1]), int(matches[1][0]))
            self.input[sensor] = beacon
            distance = self.manhattan_distance(sensor, beacon)
            self.sensor_ranges[sensor] = distance

    def manhattan_distance(self, coordinate1, coordinate2):
        y1, x1 = coordinate1
        y2, x2 = coordinate2
        return abs(x1 - x2) + abs(y1 - y2)

    def find_grid_edges(self):
        xs = [x[1] for x in self.input.keys()] + [x[1] for x in self.input.values()]
        ys = [x[0] for x in self.input.keys()] + [x[0] for x in self.input.values()]
        self.xrange = (min(xs), max(xs))
        self.yrange = (min(ys), max(ys))

    def mark_searched(self, row):
        ranges = []
        for sensor in self.sensors:
            sensor_range_on_row = self.find_range_on_row(sensor, row)
            if sensor_range_on_row:
                add_new_range = True
                ranges_to_remove = []
                for existing_range in ranges:
                    # If new range within existing range
                    if (sensor_range_on_row[0] >= existing_range[0]) and (
                        sensor_range_on_row[1] <= existing_range[1]
                    ):
                        # Don't add the new range and stop
                        add_new_range = False
                        break
                    # If existing range within new range
                    elif (sensor_range_on_row[0] <= existing_range[0]) and (
                        sensor_range_on_row[1] >= existing_range[1]
                    ):
                        # Remove existing range and continue
                        ranges_to_remove.append(existing_range)
                    # If new range overlaps with existing range
                    elif (sensor_range_on_row[0] >= existing_range[0]) and (
                        sensor_range_on_row[0] <= existing_range[1]
                    ):
                        # Combine the ranges
                        ranges_to_remove.append(existing_range)
                        sensor_range_on_row = (existing_range[0], sensor_range_on_row[1])
                    # If new range overlaps with existing range
                    elif (existing_range[0] >= sensor_range_on_row[0]) and (
                        existing_range[0] <= sensor_range_on_row[1]
                    ):
                        # Combine the ranges
                        ranges_to_remove.append(existing_range)
                        sensor_range_on_row = (sensor_range_on_row[0], existing_range[1])
                for range in ranges_to_remove:
                    ranges.remove(range)
                if add_new_range:
                    ranges.append(sensor_range_on_row)
        
        sum_ranges = 0
        for range in ranges:
            print(range)
            sum_ranges += range[1] - range[0] + 1
        sum_ranges -= self.beacons_and_sensors(row)
        return sum_ranges
                    

    # Find the range that the sensor can scan on a given row
    def find_range_on_row(self, sensor, row):
        # Find the vertical distance between the sensor and that row
        y_distance = abs(sensor[0] - row)
        # Find the range to the left and right the sensor can scan on that row
        x_range = self.sensor_ranges[sensor] - y_distance
        if x_range >= 0:
            # Return the min to max x coordinate the sensor can scan on that row
            return (sensor[1] - x_range, sensor[1] + x_range)
        else:
            return None
            
    def beacons_and_sensors(self, row):
        on_row = 0
        for i in (self.sensors + self.beacons):
            if i[0] == row:
                on_row += 1
        return on_row

    # def plot(self):
    #     # Create a mapping of unique strings to numerical values
    #     value_map = {"S": 1, "B": 2, "#": 3, "": 0}

    #     # Convert the grid to numerical values using the mapping
    #     numerical_grid = np.vectorize(value_map.get)(self.grid)

    #     # Plot the grid
    #     plt.imshow(numerical_grid, cmap="viridis")
    #     plt.colorbar(ticks=sorted(value_map.values()))
    #     plt.show()

    # def count_positions(self, row):
    #     self.mark_searched()
    #     count = 0
    #     for y, x in self.searched:
    #         if y == row:
    #             count += 1
    #     return count


filename = r"year_2022/tests/test_inputs/15_test_input.txt"
b = BeaconZone(filename)
# b.plot()
