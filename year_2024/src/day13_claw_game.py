import re
from support import support
import pandas as pd

class ClassName:
    def __init__(self, filename):
        self.file_input = support.read_input(filename, flavor=None, split_char=None)
        num_rows = len(self.file_input)
        a_pattern = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
        b_pattern = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
        prize_pattern = re.compile(r"Prize: X=(\d+), Y=(\d+)")
        self.inputs = []
        for i in range(int(num_rows / 4)):
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
        
    def cost_dataframe(self):
        df = pd.DataFrame(columns=["A presses", "B presses", "Token cost"])
        for a_presses in range(101):
            for b_presses in range(101):
                df = pd.concat([df, pd.DataFrame([{"A presses": a_presses, "B presses": b_presses, "Token cost": self.token_cost(a_presses, b_presses)}])], ignore_index=True)
        df = df.sort_values(by="Token cost", ascending=True).reset_index(drop=True)
        return df

    def part1(self):
        cost_df = self.cost_dataframe()
        tokens = 0
        for input in self.inputs:
            for _, row in cost_df.iterrows():
                a_presses = row["A presses"]
                b_presses = row["B presses"]
                x = input[0][0] * a_presses + input[1][0] * b_presses
                y = input[0][1] * a_presses + input[1][1] * b_presses
                if x == input[2][0] and y == input[2][1]:
                    tokens += row["Token cost"]
                    break
        return tokens

    def part2(self):
        pass


filename = r"year_2024/tests/test_inputs/13_test_input.txt"
# filename = r"year_2024/input/13_claw_game.txt"
m = ClassName(filename)
# m.matches
