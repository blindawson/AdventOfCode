from AdventOfCode.support import support
import numpy as np


class Seed:
    def __init__(self, filename):
        self.file_input = support.read_input(filename, flavor="split", split_char=" ")
        self.seeds = [int(x) for x in self.file_input[0][1:]]

        rows = (
            self.file_input.index(["seed-to-soil", "map:"]) + 1,
            self.file_input.index(["soil-to-fertilizer", "map:"]) - 1,
        )
        self.seed2soil = self.file_input[rows[0] : rows[1]]

        rows = (
            self.file_input.index(["soil-to-fertilizer", "map:"]) + 1,
            self.file_input.index(["fertilizer-to-water", "map:"]) - 1,
        )
        self.soil2fertilizer = self.file_input[rows[0] : rows[1]]

        rows = (
            self.file_input.index(["fertilizer-to-water", "map:"]) + 1,
            self.file_input.index(["water-to-light", "map:"]) - 1,
        )
        self.fertilizer2water = self.file_input[rows[0] : rows[1]]

        rows = (
            self.file_input.index(["water-to-light", "map:"]) + 1,
            self.file_input.index(["light-to-temperature", "map:"]) - 1,
        )
        self.water2light = self.file_input[rows[0] : rows[1]]

        rows = (
            self.file_input.index(["light-to-temperature", "map:"]) + 1,
            self.file_input.index(["temperature-to-humidity", "map:"]) - 1,
        )
        self.light2temperature = self.file_input[rows[0] : rows[1]]

        rows = (
            self.file_input.index(["temperature-to-humidity", "map:"]) + 1,
            self.file_input.index(["humidity-to-location", "map:"]) - 1,
        )
        self.temperature2humidity = self.file_input[rows[0] : rows[1]]

        rows = (
            self.file_input.index(["humidity-to-location", "map:"]) + 1,
            len(self.file_input),
        )
        self.humidity2location = self.file_input[rows[0] : rows[1]]

        self.min_loc = np.inf
        for seed in self.seeds:
            seed = int(seed)
            self.min_loc = min(self.min_loc, self.seed_path(seed))

        self.min_loc_part2 = np.inf
        for i in range(0, len(self.seeds), 2):
            print(i)
            start_range = int(self.seeds[i])
            range_len = int(self.seeds[i + 1])
            for seed in range(start_range, start_range+range_len):
                self.min_loc_part2 = min(self.min_loc_part2, self.seed_path(seed))
            

    def conversion_path(self, seed, conversion):
        destination = None
        for row in conversion:
            source_range = (int(row[1]), int(row[1]) + int(row[2]))
            destination = int(row[0])
            if (seed >= source_range[0]) and (seed <= source_range[1]):
                destination = source_range[0] + source_range[0] - destination
                break
        if not destination:
            destination = seed
        return destination

    def seed_path(self, seed):
        conversions = [
            self.seed2soil,
            self.soil2fertilizer,
            self.fertilizer2water,
            self.water2light,
            self.light2temperature,
            self.temperature2humidity,
            self.humidity2location,
        ]
        source = seed
        for conversion in conversions:
            source = self.conversion_path(source, conversion)
        # print(source)
        return source


# filename = r"year_2023/tests/test_inputs/05_test_input.txt"
filename = r"year_2023/input/05_if_you_give_a_seed_a_fertilizer.txt"

m = Seed(filename)
