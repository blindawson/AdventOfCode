from AdventOfCode.support import support
import math


class BoatRace:
    def __init__(self, filename):
        self.file_input = support.read_input(filename, flavor="split", split_char=" ")
        self.times = [int(x) for x in self.file_input[0] if x.isnumeric()]
        self.distances = [int(x) for x in self.file_input[1] if x.isnumeric()]
        self.race_results = []
        for t, d in zip(self.times, self.distances):
            self.race_results.append(self.calc_record_beaters(t, d))
        self.product = math.prod(self.race_results)

        # Part 2
        self.times_part2 = int("".join([str(x) for x in self.times]))
        self.distances_part2 = int("".join([str(x) for x in self.distances]))
        self.part2 = self.calc_record_beaters(self.times_part2, self.distances_part2)

    def calc_distance(self, time_charge: int, time_total: int):
        return time_charge * (time_total - time_charge)

    def calc_record_beaters(self, time: int, distance: int):
        for d in range(distance):
            if self.calc_distance(d, time) > distance:
                record_beaters = time + 1 - d * 2
                break
        return record_beaters
