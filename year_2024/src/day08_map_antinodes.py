from support import support
import numpy as np
import itertools


class ClassName:
    def __init__(self, filename):
        self.antennas_map = np.array(support.read_input(filename, flavor="str_grid"))
        self.antinodes_map = np.zeros(self.antennas_map.shape)
        self.antenna_names = list(set(self.antennas_map.flatten()))
        self.antenna_names.remove(".")

    def find_antinodes(self, part2=False):
        for antenna_name in self.antenna_names:
            antennas = np.where(self.antennas_map == antenna_name)
            antennas = list(zip(antennas[0], antennas[1]))
            antenna_pairs = list(itertools.combinations(antennas, 2))

            for antenna_pair in antenna_pairs:
                idx_diff = support.subtract_tuples(antenna_pair[0], antenna_pair[1])

                if part2:
                    self.antinodes_map[antenna_pair[0]] = 1
                    self.antinodes_map[antenna_pair[1]] = 1

                antinode1 = support.sum_tuples(antenna_pair[0], idx_diff)
                while not support.point_out_of_bounds(
                    y=None, x=None, grid=self.antennas_map, yx=antinode1
                ):
                    self.antinodes_map[antinode1] = 1
                    if part2:
                        antinode1 = support.sum_tuples(antinode1, idx_diff)
                    else:
                        break

                antinode2 = support.subtract_tuples(antenna_pair[1], idx_diff)
                while not support.point_out_of_bounds(
                    y=None, x=None, grid=self.antennas_map, yx=antinode2
                ):
                    self.antinodes_map[antinode2] = 1
                    if part2:
                        antinode2 = support.subtract_tuples(antinode2, idx_diff)
                    else:
                        break

        return int(self.antinodes_map.sum())
