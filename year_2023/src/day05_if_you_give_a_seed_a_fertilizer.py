from AdventOfCode.support import support
import numpy as np


class Seed:
    def __init__(self, filename):
        self.file_input = support.read_input(filename, flavor="split", split_char=" ")
        self.seeds = [int(x) for x in self.file_input[0][1:]]

        start_row = 3
        self.input_blocks = []
        for _ in range(7):
            space_index = start_row + self.file_input[start_row:].index([""])
            self.input_blocks.append(self.file_input[start_row:space_index])
            start_row = space_index + 2

        # Part 1
        self.min_loc = np.inf
        for seed in self.seeds:
            seed = int(seed)
            self.min_loc = min(self.min_loc, self.seed_path(seed))

        # Part 2
        self.min_loc_part2 = np.inf
        self.ranges = []
        for i in range(0, len(self.seeds), 2):
            start_range = int(self.seeds[i])
            range_len = int(self.seeds[i + 1])
            seed_range = (start_range, start_range + range_len)
            self.ranges.append(seed_range)
        for conversions in self.input_blocks:
            for conversion in conversions:
                self.ranges = self.process_ranges(conversion)
            for index, item in enumerate(self.ranges):
                seed1 = self.conversion_path(item[0], conversions)
                seed2 = self.conversion_path(item[1], conversions)
                self.ranges[index] = (seed1, seed2)
        self.min_loc_part2 = min([x[0] for x in self.ranges])

    def process_ranges(self, conversion):
        conversion_range = self.conversion_to_range(conversion)
        new_ranges = []
        for r in self.ranges:
            new_ranges += self.split_range(r, conversion_range)
        return new_ranges

    def conversion_to_range(self, conversion):
        range_start = int(conversion[1])
        range_end = range_start + int(conversion[2]) - 1
        return (range_start, range_end)

    def conversion_path(self, seed, conversion):
        destination = None
        for row in conversion:
            source_range = (int(row[1]), int(row[1]) + int(row[2]))
            if (seed >= source_range[0]) and (seed <= source_range[1]):
                destination = int(row[0])
                destination = seed + destination - source_range[0]
                break
        if not destination:
            destination = seed
        return destination

    def seed_path(self, seed):
        source = seed
        for conversion in self.input_blocks:
            source = self.conversion_path(source, conversion)
        # print(source)
        return source

    def split_range(self, range1: tuple, range2: tuple):
        # If range1 within range2
        if (range1[0] >= range2[0]) and (range1[1] <= range2[1]):
            # return range 1
            return [range1]
        # If range2 within range1
        elif (range1[0] < range2[0]) and (range1[1] > range2[1]):
            # Split range 1 into 3 ranges
            return [
                (range1[0], range2[0] - 1),
                (range2[0], range2[1]),
                (range2[1] + 1, range1[1]),
            ]
        # If new range overlaps with existing range
        elif (range1[0] >= range2[0]) and (range1[0] <= range2[1]):
            # Split range 1 into 2 ranges
            return [(range1[0], range2[1]), (range2[1] + 1, range1[1])]
        # If new range overlaps with existing range
        elif (range2[0] >= range1[0]) and (range2[0] <= range1[1]):
            # Split range 1 into 2 ranges
            return [(range1[0], range2[0] - 1), (range2[0], range1[1])]
        else:
            return [range1]


filename = r"year_2023/tests/test_inputs/05_test_input.txt"
# filename = r"year_2023/input/05_if_you_give_a_seed_a_fertilizer.txt"

m = Seed(filename)
