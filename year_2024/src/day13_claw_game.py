import re
from support import support
import numpy as np


class ClassName:
    def __init__(self, filename):
        self.file_input = support.read_input(filename, flavor=None, split_char=None)
        num_rows = len(self.file_input)
        a_pattern = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
        b_pattern = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
        prize_pattern = re.compile(r"Prize: X=(\d+), Y=(\d+)")
        self.inputs = []
        for i in range(int(num_rows / 4) + 1):
            a_match = a_pattern.match(self.file_input[i * 4])
            b_match = b_pattern.match(self.file_input[i * 4 + 1])
            prize_match = prize_pattern.match(self.file_input[i * 4 + 2])

            a_x = int(a_match.group(1))
            a_y = int(a_match.group(2))
            b_x = int(b_match.group(1))
            b_y = int(b_match.group(2))
            prize_x = int(prize_match.group(1))
            prize_y = int(prize_match.group(2))
            self.inputs.append([(a_x, a_y), (b_x, b_y), (prize_x, prize_y)])

    def token_cost(self, a_presses, b_presses):
        return a_presses * 3 + b_presses

    def run_input(self, part2=False):
        tokens = 0
        input_num = 0
        for input in self.inputs:
            input_num += 1
            a_x, a_y = input[0]
            b_x, b_y = input[1]
            prize_x, prize_y = input[2]
            if part2:
                prize_x += 10000000000000
                prize_y += 10000000000000

            a = np.array([[a_x, b_x], [a_y, b_y]])
            b = np.array([prize_x, prize_y])
            c = np.linalg.solve(a, b)
            c_round = [round(val) for val in c]

            if all(val >= 0 for val in c_round):
                x = a_x * c_round[0] + b_x * c_round[1]
                y = a_y * c_round[0] + b_y * c_round[1]
                if x == prize_x and y == prize_y:
                    tokens += self.token_cost(c_round[0], c_round[1])
                else:
                    print("nope")
                print(input_num, [abs(round(i - j, 3)) for i, j in zip(c, c_round)])

        return int(tokens)
