from AdventOfCode.support import support
import numpy as np


class BeamReflector:
    def __init__(self, filename):
        self.file_input = np.array(support.read_input(filename, flavor="str_grid"))

    beam_dict = {
        ("E", "|"): ["N", "S"],
        ("W", "|"): ["N", "S"],
        ("N", "|"): ["N"],
        ("S", "|"): ["S"],
        ("E", "-"): ["E"],
        ("W", "-"): ["W"],
        ("N", "-"): ["E", "W"],
        ("S", "-"): ["E", "W"],
        ("E", "/"): ["N"],
        ("W", "/"): ["S"],
        ("N", "/"): ["E"],
        ("S", "/"): ["W"],
        ("E", "\\"): ["S"],
        ("W", "\\"): ["N"],
        ("N", "\\"): ["W"],
        ("S", "\\"): ["E"],
        ("W", "."): ["W"],
        ("N", "."): ["N"],
        ("S", "."): ["S"],
        ("E", "."): ["E"],
    }

    def def_bean(self, loc, dir):
        return {"loc": loc, "dir": dir}

    def move_beam(self, start_loc=(0,0), start_dir="E"):
        beam_map = np.zeros(self.file_input.shape, dtype=int)
        previous_beams = np.empty(self.file_input.shape, dtype=object)
        previous_beams[:] = [
            [[] for _ in range(self.file_input.shape[1])]
            for _ in range(self.file_input.shape[0])
        ]
        beams = [self.def_bean(start_loc, start_dir)]
        beam_map[beams[0]["loc"]] = 1
        while beams:
            new_beams = []
            remove_indices = []
            for index, beam in enumerate(beams):
                new_dirs = self.beam_dict[(beam["dir"], self.file_input[beam["loc"]])]
                new_locs = [
                    support.sum_tuples(beam["loc"], support.direction_dict[d])
                    for d in new_dirs
                ]
                if (
                    support.point_out_of_bounds(
                        new_locs[0][0], new_locs[0][1], self.file_input
                    )
                    or new_dirs[0] in previous_beams[new_locs[0]]
                ):
                    remove_indices.append(index)
                else:
                    beams[index] = self.def_bean(new_locs[0], new_dirs[0])
                    beam_map[new_locs[0]] = 1
                    previous_beams[new_locs[0]].append(new_dirs[0])
                if len(new_dirs) > 1:
                    if (
                        not support.point_out_of_bounds(
                            new_locs[1][0], new_locs[1][1], self.file_input
                        )
                        and not new_dirs[1] in previous_beams[new_locs[1]]
                    ):
                        new_beams.append(self.def_bean(new_locs[1], new_dirs[1]))
                        beam_map[new_locs[1]] = 1
                        previous_beams[new_locs[1]].append(new_dirs[1])
            for i in sorted(remove_indices, reverse=True):
                beams.pop(i)
            beams += new_beams
        return sum(sum(beam_map))
        
    def find_beam(self):
        max_beams = 0
        for y in range(self.file_input.shape[0]):
            max_beams = max(max_beams, self.move_beam((y, 0), "E"))
            max_beams = max(max_beams, self.move_beam((y, self.file_input.shape[1]-1), "W"))
        for x in range(self.file_input.shape[1]):
            max_beams = max(max_beams, self.move_beam((0, x), "S"))
            max_beams = max(max_beams, self.move_beam((self.file_input.shape[0]-1, x), "N"))
        return max_beams
            


filename = r"year_2023/tests/test_inputs/16_test_input.txt"
m = BeamReflector(filename)
m.move_beam()
