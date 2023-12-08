from AdventOfCode.support import support
from math import gcd


class ClassName:
    def __init__(self, filename, part2=False):
        self.file_input = support.read_input(filename, flavor="split", split_char=" ")
        self.directions = self.file_input[0][0]
        self.part2 = part2
        self.network = {}
        self.create_network()
        if not part2:
            self.nodes = ["AAA"]
        else:
            self.nodes = [x for x in self.network.keys() if x[-1] == "A"]
        self.steps = []
        for node in self.nodes:
            self.steps.append(self.find_step_to_z(node))
        self.total_steps = self.calc_lcm(self.steps)

    def calc_direction(self, step: int):
        direction_dict = {"L": 0, "R": 1}
        direction_letter = self.directions[step % len(self.directions)]
        direction_index = direction_dict[direction_letter]
        return direction_index

    def create_network(self):
        for i in self.file_input[2:]:
            node = i[0]
            dir1 = i[2][1:-1]
            dir2 = i[3][:-1]
            self.network[node] = (dir1, dir2)

    def find_step_to_z(self, node):
        step = 0
        at_end = False
        while not at_end:
            direction_index = self.calc_direction(step)
            node = self.network[node][direction_index]
            step += 1
            if not self.part2:
                at_end = node == "ZZZ"
            else:
                at_end = node[-1] == "Z"
        return step

    def calc_lcm(self, nums: list):
        lcm = 1
        for i in nums:
            lcm = lcm * i // gcd(lcm, i)
        return lcm
