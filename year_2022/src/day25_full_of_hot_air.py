from AdventOfCode.support import support


class HotAir:
    def __init__(self, filename):
        self.file_input = support.read_input(filename, flavor=None, split_char=None)
        self.n5_dict = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
        self.n10_dict = {
            4: ("-", 1),
            3: ("=", 1),
            2: ("2", 0),
            1: ("1", 0),
            0: ("0", 0),
        }

    def convert_to_num10(self, num5: str):
        num10 = 0
        for index, n in enumerate(num5[::-1]):
            num10 += self.n5_dict[n] * 5**index
        return num10

    def sum_input(self):
        s = 0
        for i in self.file_input:
            s += self.convert_to_num10(i)
        return s

    def convert_to_num5(self, num10: int, ans: str = "", power: int = 0):
        if num10 > 0:
            quotient = num10 / 5**power
            remainder = int(quotient % 5)
            ans = self.n10_dict[remainder][0] + ans
            num10 = (
                num10
                - (remainder * 5**power)
                + self.n10_dict[remainder][1] * 5 ** (power + 1)
            )
            ans = self.convert_to_num5(num10, ans, power + 1)
        return ans


filename = r"year_2022/tests/test_inputs/25_test_input.txt"
m = HotAir(filename)
m.convert_to_num5(2022)
