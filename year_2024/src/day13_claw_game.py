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

    def cost_dataframe(self, range_a=101, range_b=101):
        df = pd.DataFrame(columns=["A presses", "B presses", "Token cost"])
        for a_presses in range(range_a):
            for b_presses in range(range_b):
                df = pd.concat(
                    [
                        df,
                        pd.DataFrame(
                            [
                                {
                                    "A presses": a_presses,
                                    "B presses": b_presses,
                                    "Token cost": self.token_cost(a_presses, b_presses),
                                }
                            ]
                        ),
                    ],
                    ignore_index=True,
                )
        df = df.sort_values(by="Token cost", ascending=True).reset_index(drop=True)
        return df

    # solving for ax + by = gcd(a,b)
    def extended_euclidian(self, a, b):
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = b // a, b % a
            m, n = x - u * q, y - v * q
            b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
        return gcd, x, y
        
    def lcm(self, a, b):
        return abs(a * b) // self.extended_euclidian(a, b)[0]

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
        tokens = 0
        for input in self.inputs:
            a_x, a_y = input[0]
            b_x, b_y = input[1]
            prize_x, prize_y = input[2]
            # prize_x += 10000000000000
            # prize_y += 10000000000000

            gcd_x, axn, bxn = self.extended_euclidian(a_x, b_x)
            if prize_x % gcd_x != 0:
                break

            gcd_y, ayn, byn = self.extended_euclidian(a_y, b_y)
            if prize_y % gcd_y != 0:
                break

            scale_x = prize_x // gcd_x
            axn *= scale_x
            bxn *= scale_x
            kx_min = axn // (b_x // gcd_x)
            kx_max = -bxn // (a_x // gcd_x)

            scale_y = prize_y // gcd_y
            ayn *= scale_y
            byn *= scale_y

            solutions = []
            for kx in range(kx_min, kx_max + 1):
                x = axn + kx * (b_x // gcd_x)
                y = ayn + kx * (b_y // gcd_y)
                if x == prize_x and y == prize_y:
                    solutions.append(self.token_cost(x / a_x, y / a_y))
                    print(x / a_x, y / a_y)

            if solutions:
                tokens += min(solutions)
        return tokens
    
    def part2a(self):
        tokens = 0
        input_num = 0
        for input in self.inputs:
            input_num += 1
            a_x, a_y = input[0]
            b_x, b_y = input[1]
            prize_x, prize_y = input[2]
            prize_x += 10000000000000
            prize_y += 10000000000000

            gcd_x, axn, bxn = self.extended_euclidian(a_x, b_x)
            if prize_x % gcd_x != 0:
                continue

            gcd_y, ayn, byn = self.extended_euclidian(a_y, b_y)
            if prize_y % gcd_y != 0:
                continue
                
            lcm_x = self.lcm(a_x, b_x)
            lcm_y = self.lcm(a_y, b_y)
            
            # start with just the x
            # the scale is based on the prize divided by the lcm
            scale_x = prize_x // lcm_x
            target_start_x = (scale_x - 1) * lcm_x
            
            # figure out the cheapest way to get to scale_x * lcm_x
            a_price = 3 * target_start_x / a_x
            b_price = 1 * target_start_x / b_x
            if a_price < b_price:
                # start with x button presses
                a_start = target_start_x / a_x
                b_start = 0
                start_price = a_price
            else:
                # start with y button presses
                a_start = 0
                b_start = target_start_x / b_x
                start_price = b_price
            target_start_y = a_y * a_start + b_y * b_start
                
            # now we are searching around target_start_x
            # we will iterate over enough a-button presses to cover lcm_x*2
            k_a = int(lcm_x / a_x * 2)
            # same for b
            k_b = int(lcm_x / b_x * 2)
            print(input_num, k_a, k_b)
            
            # now make a dataframe and sort by cost
            df = self.cost_dataframe(range_a=k_a, range_b=k_b)
            for _, row in df.iterrows():
                a_presses = row["A presses"]
                b_presses = row["B presses"]
                x = a_x * a_presses + b_x * b_presses + target_start_x
                y = a_y * a_presses + b_y * b_presses + target_start_y
                if x == prize_x and y == prize_y:
                    tokens += row["Token cost"] + start_price
                    break
        return int(tokens)
            
            
    def print_lcm(self):
        for input in self.inputs:
            a_x, a_y = input[0]
            b_x, b_y = input[1]
            print(self.lcm(a_x, b_x), self.lcm(a_y, b_y))
            print(input[2])
            print(a_x, b_x, a_y, b_y)
            print()


filename = r"year_2024/tests/test_inputs/13_test_input.txt"
filename = r"year_2024/input/13_claw_game.txt"
m = ClassName(filename)
# m.matches
m.part2a()
